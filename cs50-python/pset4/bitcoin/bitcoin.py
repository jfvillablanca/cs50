import sys

import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json", timeout=1
    )
except (requests.RequestException, requests.Timeout) as error:
    sys.exit(f"Request error:\n{error}")

bitcoin_rate = response.json()["bpi"]["USD"]["rate_float"]
print(f"${bitcoin_rate * bitcoin:,.4f}")
