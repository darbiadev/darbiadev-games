"""test games"""

from darbia.games.tabletop.helpers import bulk_random_numbers


def test_sample() -> None:
    """sample test"""
    assert bulk_random_numbers(3, 1) == ([1, 1, 1], 3)
