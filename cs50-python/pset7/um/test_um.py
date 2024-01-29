from um import count


def test_single_um():
    assert count("hello, um, world, um, hi") == 2


def test_distinguish_um_inside_word():
    assert count("the penumbra, um, is a type of, um, shadow") == 2


def test_count_um_even_with_a_lot_of_whitespace():
    assert count("um     um   um    um um") == 5


def test_insensitively_distinguish_um():
    assert count("Um, hello, um, world, UM, hi") == 3
