"""
We want a function called
``count_returns_in_leading_whitespace``
that takes a string and
returns the number of newlines in the leading
whitespace of that string.
"""

from pytest import mark
from .get_leading_whitespace import get_leading_whitespace

@mark.parametrize(
    "test_input,expected_output",
    [(" ", 0), ("\n", 1), ("\n ", 1), ("\n\n", 2), ("\n\n ", 2)],
)
def test_count_returns_in_leading_whitespace(test_input, expected_output):
    assert count_returns_in_leading_whitespace(test_input) == expected_output

class LeadingWhitespace(str):
    """
    Leading whitespace of a string, usually a string of source code.
    """

class NumberOfReturnsInLeadingWhitespace(int):
    """
    Number of newlines in the leading whitespace of a string.
    """

def count_returns_in_leading_whitespace(s: LeadingWhitespace) -> NumberOfReturnsInLeadingWhitespace:
    """
    Count the number of newlines in the leading whitespace of a string.

    Parameters
    ----------
    s : ``LeadingWhitespace``
        The string to count the newlines in the leading whitespace of.

    Returns
    -------
    ``NumberOfReturnsInLeadingWhitespace``
        The number of newlines in the leading whitespace of the string.

    Examples
    --------
    >>> count_returns_in_leading_whitespace("")
    0
    >>> count_returns_in_leading_whitespace(" ")
    0
    >>> count_returns_in_leading_whitespace("\n")
    1
    >>> count_returns_in_leading_whitespace("\n ")
    1
    >>> count_returns_in_leading_whitespace("\n\n")
    2
    >>> count_returns_in_leading_whitespace("\n\n ")
    2
    """

    # write the body of the function

    s = get_leading_whitespace(s)

    return s.count("\n")
