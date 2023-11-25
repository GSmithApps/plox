"""
A function that, when given a string of source code,
it will return the first token and the number of new lines
in that token (if it is a string literal).
"""

from typing import Tuple
from .token.token import Token
from .token.tokentype import TokenType
from .token.tokentype.token_dicts import SINGLE_CHARACTER_TOKENS
from .token.tokentype.two_character_token_dicts import TWO_CHARACTER_TOKENS
from .token.two_character_tokens import two_character_tokens
from .token.single_character_tokens import single_character_tokens

def test_get_next_token_ignoring_whitespace_empty_string():
    assert get_next_token_ignoring_whitespace('') is None

def test_get_next_token_ignoring_whitespace_single_left_paren():
    assert get_next_token_ignoring_whitespace('(') == (Token(TokenType.LEFT_PAREN, '(', None), 0)

def test_get_next_token_ignoring_whitespace_single_right_paren():
    assert get_next_token_ignoring_whitespace(')') == (Token(TokenType.RIGHT_PAREN, ')', None), 0)

def test_get_next_token_ignoring_whitespace_multiple_tokens():
    assert get_next_token_ignoring_whitespace('()') == (Token(TokenType.LEFT_PAREN, '(', None), 0)


def get_next_token_ignoring_whitespace(source_code: str) -> Tuple[Token, int]:
    """
    Ignore whitespace and return the first token in the source code.

    - If the source code is empty, return an EOF token.
    - If the source code starts with a single character token, return that token.
    - If the source code starts with the first character of
      a two character token, 
    """
    source_code = source_code.lstrip()

    if not source_code:
        return (Token(TokenType.EOF, '', None), 0)

    elif source_code[0] in SINGLE_CHARACTER_TOKENS:
        return single_character_tokens(source_code)

    elif source_code[0] in TWO_CHARACTER_TOKENS:
        return two_character_tokens(source_code)

    elif source_code[0] == '/':
        return process_leading_slash(source_code)

