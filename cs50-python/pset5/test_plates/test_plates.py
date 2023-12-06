from plates import is_valid


def test_start_with_at_least_two_letters():
    assert is_valid("XX") is True
    assert is_valid("X0") is False


def test_must_contain_alphabetic_characters():
    assert is_valid("XX1234") is True
    assert is_valid("123456") is False


def test_contains_two_to_six_characters():
    assert is_valid("ABCDEF") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_must_not_contain_numbers_in_between():
    assert is_valid("CS50P") is False


def test_first_digit_cannot_be_zero():
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False


def test_punctuation_is_not_allowed():
    assert is_valid("CS..") is False
