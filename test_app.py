from app import random_fruit


def test_fruit():
    assert "orange" or "banana" or "apple" is random_fruit()
