import pytest

from working import convert


def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_with_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_with_mixed_minutes():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("5:30 PM to 9 AM") == "17:30 to 09:00"
    assert convert("12:59 PM to 12:01 AM") == "12:59 to 00:01"


def test_omitted_to():
    with pytest.raises(ValueError):
        convert("12:59 PM 12:01 AM")


def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("12:69 PM to 12:01 AM")
