from pytest import raises

from fuel import convert, gauge


def test_zero_division():
    with raises(ZeroDivisionError):
        convert("1/0")


def test_non_integer():
    with raises(ValueError):
        convert("1.5/2")

    with raises(ValueError):
        convert("cat/2")


def test_valid_input():
    assert convert("1/2") == 50


def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_regular_fuel():
    assert gauge(50) == "50%"
