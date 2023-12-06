from twttr import shorten


def test_lowercase():
    assert shorten("aeiou") == ""


def test_uppercase():
    assert shorten("hELLo") == "hLL"


def test_numbers():
    assert shorten("hell0") == "hll0"


def test_punctuation():
    assert shorten(".") == "."
