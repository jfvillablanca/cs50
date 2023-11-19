import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from flask_session import Session
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    total_stock_valuation = 0

    user_cash_balance = db.execute(
        "SELECT cash FROM users WHERE id = ?", session["user_id"]
    )[0]["cash"]
    assets = db.execute(
        "SELECT user_id, symbol, SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE -shares END) AS share_count FROM transactions GROUP BY symbol, user_id HAVING user_id = ?",
        session["user_id"],
    )
    for asset in assets:
        current_price = lookup(asset["symbol"])["price"]
        stock_valuation = current_price * asset["share_count"]
        asset["stock_valuation"] = stock_valuation
        total_stock_valuation += stock_valuation

    return render_template(
        "index.html",
        balance=user_cash_balance,
        total_stock_valuation=total_stock_valuation,
        total=total_stock_valuation + user_cash_balance,
        assets=assets,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
    balance = float(user["cash"])

    if request.method == "POST":
        if not request.form.get("symbol"):
            redirect("/buy")

        if not request.form.get("shares"):
            redirect("/buy")

        lookedup_quote = lookup(request.form.get("symbol"))
        if lookedup_quote is None:
            return apology("please enter a valid symbol")

        try:
            shares = int(request.form.get("shares"))
            if shares <= 0:
                return apology("Please submit a valid shares amount")
        except ValueError:
            return apology("Please submit a valid shares amount")

        symbol = lookedup_quote["symbol"]
        price = lookedup_quote["price"]

        total_buy_amount = shares * price

        if total_buy_amount > balance:
            return apology("cannot afford the total amount")

        balance -= total_buy_amount

        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"]
        )
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, transaction_type) VALUES(?, ?, ?, ?, ?)",
            session["user_id"],
            symbol,
            shares,
            price,
            "buy",
        )
        return redirect("/")

    return render_template("buy.html", balance=balance)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = ?",
        session["user_id"],
    )
    for transaction in transactions:
        transaction["total"] = transaction["shares"] * transaction["price"]

    return render_template(
        "history.html",
        transactions=transactions,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/changepw", methods=["GET", "POST"])
def change_pw():
    """Change password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("currentpassword"):
            return apology("must provide correct password", 403)

        elif not request.form.get("newpassword"):
            return apology("must provide new password")

        current_hash = db.execute(
            "SELECT hash FROM users WHERE id = ?", session["user_id"]
        )[0]["hash"]

        # Ensure username exists and password is correct
        if not check_password_hash(current_hash, request.form.get("currentpassword")):
            return apology("invalid password", 403)

        hashed_new_pw = generate_password_hash(request.form.get("newpassword"))

        db.execute(
            "UPDATE users SET hash = ? WHERE id = ?", hashed_new_pw, session["user_id"]
        )

        return redirect("/")

    else:
        return render_template("changepw.html")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        if not request.form.get("symbol"):
            redirect("/quote")

        lookedup_quote = lookup(request.form.get("symbol"))
        if lookedup_quote is None:
            return apology("please enter a valid symbol")

        return render_template("quoted.html", quote=lookedup_quote)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Query database to check if username already exists
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        if len(rows) != 0:
            return apology("username already exists")

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirm password must match")

        username = request.form.get("username")
        hashed_pw = generate_password_hash(request.form.get("password"))

        # Create new user
        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed_pw
        )

        # Get the newly created user
        user = db.execute(
            "SELECT * FROM users WHERE username = ? LIMIT 1",
            request.form.get("username"),
        )[0]

        # Automatically log in the newly registered user
        session["user_id"] = user["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
    balance = float(user["cash"])

    assets = db.execute(
        "SELECT user_id, symbol, SUM(CASE WHEN transaction_type = 'buy' THEN shares ELSE -shares END) AS share_count FROM transactions GROUP BY symbol, user_id HAVING user_id = ?",
        session["user_id"],
    )

    if request.method == "POST":
        # Symbol validation
        symbol = request.form.get("symbol")
        if symbol not in [a["symbol"] for a in assets]:
            return apology("Please select a valid symbol")

        # Shares validation
        for asset in assets:
            if asset["symbol"] == symbol:
                shares_available = asset["share_count"]

        try:
            shares_to_sell = float(request.form.get("shares"))
            if shares_to_sell <= 0 or shares_to_sell > shares_available:
                return apology("Please submit a valid shares amount")
        except ValueError:
            return apology("Please submit a valid shares amount")

        price = lookup(symbol)["price"]

        total_sell_amount = shares_to_sell * price

        balance += total_sell_amount

        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"]
        )
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, transaction_type) VALUES(?, ?, ?, ?, ?)",
            session["user_id"],
            symbol,
            shares_to_sell,
            price,
            "sell",
        )
        return redirect("/")

    return render_template("sell.html", assets=assets)
