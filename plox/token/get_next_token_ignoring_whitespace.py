"""
A function that, when given a string of source code,
it will return the first token and the number of new lines
in that token (if it is a string literal).
"""

from typing import Tuple
from .token import Token
from .tokentype import TokenType
from .tokentype.token_dicts import SINGLE_CHARACTER_TOKENS
from .tokentype.two_character_token_dicts import (
    TWO_CHARACTER_TOKENS, TWO_CHARACTER_TOKEN_ONLY_FIRST,
    TWO_CHARACTER_TOKEN_BOTH
)

def test_get_next_token_ignoring_whitespace_empty_string():
    assert get_next_token_ignoring_whitespace('') is None

def test_get_next_token_ignoring_whitespace_single_left_paren():
    assert get_next_token_ignoring_whitespace('(') == (Token(TokenType.LEFT_PAREN, '(', None), 0)

def test_get_next_token_ignoring_whitespace_single_right_paren():
    assert get_next_token_ignoring_whitespace(')') == (Token(TokenType.RIGHT_PAREN, ')', None), 0)

def test_get_next_token_ignoring_whitespace_multiple_tokens():
    assert get_next_token_ignoring_whitespace('()') == (Token(TokenType.LEFT_PAREN, '(', None), 0)


def get_next_token_ignoring_whitespace(source_code: str) -> Tuple[Token, int]:
    source_code = source_code.lstrip()

    if not source_code:
        return (TokenType.EOF, 0)

    if source_code[0] in SINGLE_CHARACTER_TOKENS:
        return (Token(SINGLE_CHARACTER_TOKENS[source_code[0]], source_code[0], None), 0)

    if source_code[0] in TWO_CHARACTER_TOKENS:
        expected = TWO_CHARACTER_TOKENS[source_code[0]]
        if source_code[1] == expected:
            return (Token(TWO_CHARACTER_TOKEN_BOTH[source_code[0]], source_code[0:2], None), 0)
        else:
            return (Token(TWO_CHARACTER_TOKEN_ONLY_FIRST[source_code[0]], source_code[0], None), 0)
    



            