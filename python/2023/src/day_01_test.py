import pytest
from .day_01 import extract_two_digit_number


@pytest.mark.parametrize(
    "actual,expected",
    [
        ("", 0),
        ("cat", 0),
        ("9cbncbxclbvkmfzdnldc", 9),
        ("jjn1drdffhs", 11),
        ("3six7", 37),
        ("38rgtnqqxtc", 38),
        ("rxszdkkv3j8kjhbm", 38),
        ("kqgthcleightsixeight96nine69", 99),
        ("23onezbvbrlnseven239", 29),
    ],
)
def test_extract_two_digit_number(actual: str, expected: int):
    assert extract_two_digit_number(actual) == expected
