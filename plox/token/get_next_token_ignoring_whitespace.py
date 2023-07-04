"""
A function that, when given a string of source code,
it will return the first token and the number of new lines
in that token (if it is a string literal).
"""

from typing import Tuple
from .token import Token
from .tokentype import TokenType

def test_get_next_token_ignoring_whitespace_empty_string():
    assert get_next_token_ignoring_whitespace('') is None

def test_get_next_token_ignoring_whitespace_single_left_paren():
    assert get_next_token_ignoring_whitespace('(') == Token(TokenType.LEFT_PAREN, '(', None, 1)

def test_get_next_token_ignoring_whitespace_single_right_paren():
    assert get_next_token_ignoring_whitespace(')') == Token(TokenType.RIGHT_PAREN, ')', None, 1)

def test_get_next_token_ignoring_whitespace_multiple_tokens():
    assert get_next_token_ignoring_whitespace('()') == Token(TokenType.LEFT_PAREN, '(', None, 1)


def get_next_token_ignoring_whitespace(source_code: str) -> Tuple[Token, int]:
    source_code = source_code.lstrip()

