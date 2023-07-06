"""
We want a function to process the two character tokens.
"""

from pytest import mark
from .tokentype.two_character_token_dicts import (
    TWO_CHARACTER_TOKENS, TWO_CHARACTER_TOKEN_ONLY_FIRST, TWO_CHARACTER_TOKEN_BOTH
)
from .token import Token


@mark.parametrize('source_code, expected', [
    ('!=', (Token(TWO_CHARACTER_TOKEN_BOTH['!'], '!=', None), 0)),
    ('==', (Token(TWO_CHARACTER_TOKEN_BOTH['='], '==', None), 0)),
    ('>=', (Token(TWO_CHARACTER_TOKEN_BOTH['>'], '>=', None), 0)),
    ('<=', (Token(TWO_CHARACTER_TOKEN_BOTH['<'], '<=', None), 0))
])
def test_two_character_tokens_with_match(source_code, expected):
    assert two_character_tokens(source_code) == expected


@mark.parametrize('source_code, expected', [
    ('!>', (Token(TWO_CHARACTER_TOKEN_ONLY_FIRST['!'], '!', None), 0)),
    ('=>', (Token(TWO_CHARACTER_TOKEN_ONLY_FIRST['='], '=', None), 0)),
    ('>>', (Token(TWO_CHARACTER_TOKEN_ONLY_FIRST['>'], '>', None), 0)),
    ('<<', (Token(TWO_CHARACTER_TOKEN_ONLY_FIRST['<'], '<', None), 0))
])
def test_two_character_tokens_without_match(source_code, expected):
    assert two_character_tokens(source_code) == expected



def two_character_tokens(source_code):
    expected = TWO_CHARACTER_TOKENS[source_code[0]]
    if source_code[1] == expected:
        x = (Token(TWO_CHARACTER_TOKEN_BOTH[source_code[0]], source_code[0:2], None), 0)
    else:
        x = (Token(TWO_CHARACTER_TOKEN_ONLY_FIRST[source_code[0]], source_code[0], None), 0)
    return x
