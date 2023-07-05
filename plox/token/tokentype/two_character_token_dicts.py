"""
We want three dictionaries:

- a dictionary that maps from the first match
  to the second match, such as bang to equals
- a dictionary that maps the first match to
  the token type if the second match is not
  found
- a dictionary that maps the first match to
  the token type if the second match is found
"""

from pytest import mark
from . import TokenType

@mark.parametrize('first_match, expected', [
    ('!', '='),
    ('=', '='),
    ('>', '='),
    ('<', '=')
])
def test_two_character_token_dicts_has_desired_first_matches(first_match, expected):
    assert TWO_CHARACTER_TOKENS[first_match] == expected

@mark.parametrize('first_match, expected', [
    ('!', TokenType.BANG),
    ('=', TokenType.EQUAL),
    ('>', TokenType.GREATER),
    ('<', TokenType.LESS)
])
def test_two_character_token_dicts_has_desired_token_types(first_match, expected):
    assert TWO_CHARACTER_TOKEN_ONLY_FIRST[first_match] == expected

@mark.parametrize('first_match, expected', [
    ('!', TokenType.BANG_EQUAL),
    ('=', TokenType.EQUAL_EQUAL),
    ('>', TokenType.GREATER_EQUAL),
    ('<', TokenType.LESS_EQUAL)
])
def test_two_character_token_dicts_has_desired_token_types(first_match, expected):
    assert TWO_CHARACTER_TOKEN_BOTH[first_match] == expected

TWO_CHARACTER_TOKENS = {
    '!': '=',
    '=': '=',
    '>': '=',
    '<': '='
}

TWO_CHARACTER_TOKEN_ONLY_FIRST = {
    '!': TokenType.BANG,
    '=': TokenType.EQUAL,
    '>': TokenType.GREATER,
    '<': TokenType.LESS
}

TWO_CHARACTER_TOKEN_BOTH = {
    '!': TokenType.BANG_EQUAL,
    '=': TokenType.EQUAL_EQUAL,
    '>': TokenType.GREATER_EQUAL,
    '<': TokenType.LESS_EQUAL
}

