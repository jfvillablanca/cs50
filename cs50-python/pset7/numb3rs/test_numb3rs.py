from numb3rs import validate


def test_nonnumeric_ip_input():
    assert validate("cat") is False


def test_valid_ip_input():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True


def test_invalid_ip_input_but_first_byte_is_valid():
    assert validate("255.256.0.1") is False


def test_invalid_ip_input():
    assert validate("512.0.0.1") is False
    assert validate("275.3.6.28") is False


def test_invalid_ip_input_too_much_octets():
    assert validate("255.255.255.255.255") is False
