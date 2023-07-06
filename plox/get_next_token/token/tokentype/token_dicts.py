"""
Make a dictionary of the single element tokens

The slash is a single character token (
when used for division),
but it is not in the dictionary because
it can be used as a comment character,
which is two characters.
"""

from typing import Dict
from . import TokenType
from pytest import mark

# write a test to ensure that the
# single character tokens are mapped
# to the correct token type

@mark.parametrize('character, token_type', [
    ('(', TokenType.LEFT_PAREN),
    (')', TokenType.RIGHT_PAREN),
    ('{', TokenType.LEFT_BRACE),
    ('}', TokenType.RIGHT_BRACE),
    (',', TokenType.COMMA),
    ('.', TokenType.DOT),
    ('-', TokenType.MINUS),
    ('+', TokenType.PLUS),
    (';', TokenType.SEMICOLON),
    ('*', TokenType.STAR),
])
def test_single_character_tokens(character: str, token_type: TokenType):
    assert SINGLE_CHARACTER_TOKENS[character] == token_type

# slash isn't in here
SINGLE_CHARACTER_TOKENS: Dict[str, TokenType] = {
    '(': TokenType.LEFT_PAREN,
    ')': TokenType.RIGHT_PAREN,
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    ',': TokenType.COMMA,
    '.': TokenType.DOT,
    '-': TokenType.MINUS,
    '+': TokenType.PLUS,
    ';': TokenType.SEMICOLON,
    '*': TokenType.STAR,
}

