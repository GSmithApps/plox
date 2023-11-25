"""
We need a function that takes a string and returns
its leading whitespace.
"""

from pytest import mark

@mark.parametrize(
    "test_input,expected_output",
    [
        ("", ""),
        (" ", " "),
        ("\n", "\n"),
        ("\n ", "\n "),
        ("\n\n", "\n\n"),
        ("\n\n ", "\n\n "),
        ("some text", ""),
        (" some text", " "),
        ("\nsome text", "\n"),
        ("\tsome text", "\t"),
    ],
)
def test_get_leading_whitespace(test_input, expected_output):
    assert get_leading_whitespace(test_input) == expected_output

# implement the function

class SourceCodeWithLeadingWhitespace(str):
    """
    String of source code with leading whitespace.

    - ``" some text"``
    - ``"\t  some text"``
    """

class LeadingWhitespaceFromSourceCode(str):
    """
    Leading whitespace from source code.

    - ``" "``
    - ``"\t "``
    """

def get_leading_whitespace(
    s: SourceCodeWithLeadingWhitespace
) -> LeadingWhitespaceFromSourceCode:
    """
    Get the leading whitespace of a string of source code.

    Parameters
    ----------
    s : str
        The string to get the leading whitespace of.

    Returns
    -------
    str
        The leading whitespace of the string.

    Examples
    --------
    >>> get_leading_whitespace("")
    ''
    >>> get_leading_whitespace(" ")
    ' '
    >>> get_leading_whitespace("\n")
    '\\n'
    >>> get_leading_whitespace("\n ")
    '\\n '
    >>> get_leading_whitespace("\n\n")
    '\\n\\n'
    >>> get_leading_whitespace("\n\n ")
    '\\n\\n '
    >>> get_leading_whitespace("some text")
    ''
    >>> get_leading_whitespace(" some text")
    ' '
    """

    return s[:len(s) - len(s.lstrip())]