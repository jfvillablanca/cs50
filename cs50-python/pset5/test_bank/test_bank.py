from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("h") == 20
    assert value("H") == 20
    assert value("heart") == 20


def test_nonhello():
    assert value("what's up") == 100
