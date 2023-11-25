"""
We want a function called ``increment_line_using_leading_whitespace`` 
that takes a string and a line number and returns the line number
incremented by the number of newlines in the leading whitespace of the string.
"""

from pytest import mark
from .count_returns_in_leading_whitespace import count_returns_in_leading_whitespace

@mark.parametrize(
    "test_input,expected_output",
    [
        ("", 0),
        (" ", 0),
        ("\n", 1),
        ("\n ", 1),
        ("\n\n", 2),
        ("\n\n ", 2),
        ("some text", 0),
        (" some text", 0),
        ("\nsome text", 1),
    ],
)
def test_increment_line_using_leading_whitespace(test_input, expected_output):
    assert increment_line_using_leading_whitespace(test_input, 0) == expected_output


class LineNumberBeforeIncrement(int):
    """
    The line number before incrementing.
    """

class LineNumberAfterIncrement(int):
    """
    The line number after incrementing
    the line number according to the number of newlines
    in the leading whitespace of a string.

    This will be the starting line number for
    subsequent lines of source code.
    """

class SourceCodeWithLeadingWhitespace(str):
    """
    - ``" some text"``
    - ``"\\n\\n "``
    """

def increment_line_using_leading_whitespace(
        s: SourceCodeWithLeadingWhitespace,
        line: LineNumberBeforeIncrement
    ) -> LineNumberAfterIncrement:
    """
    Increment a line number by the number of newlines in the leading whitespace of a string.

    Parameters
    ----------
    s : str
        The string to count the newlines in the leading whitespace of.
    line : int
        The line number to increment.

    Returns
    -------
    int
        The line number incremented by the number of newlines in the leading whitespace of the string.

    Examples
    --------
    >>> increment_line_using_leading_whitespace("", 0)
    0
    >>> increment_line_using_leading_whitespace(" ", 0)
    0
    >>> increment_line_using_leading_whitespace("\\n", 0)
    1
    >>> increment_line_using_leading_whitespace("\\n ", 0)
    1
    >>> increment_line_using_leading_whitespace("\\n\\n", 0)
    2
    >>> increment_line_using_leading_whitespace("\\n\\n ", 0)
    2
    >>> increment_line_using_leading_whitespace("some text", 0)
    0
    >>> increment_line_using_leading_whitespace(" some text", 0)
    0
    >>> increment_line_using_leading_whitespace("\\nsome text", 0)
    1
    """

    # write the body of the function

    return line + count_returns_in_leading_whitespace(s)