"""
We want a function to process the single
character tokens.
"""

from pytest import mark
from .token import Token
from .tokentype.token_dicts import SINGLE_CHARACTER_TOKENS


@mark.parametrize('source_code, expected', [
    ('(', (Token(SINGLE_CHARACTER_TOKENS['('], '(', None), 0)),
    (')', (Token(SINGLE_CHARACTER_TOKENS[')'], ')', None), 0)),
    ('{', (Token(SINGLE_CHARACTER_TOKENS['{'], '{', None), 0)),
    ('}', (Token(SINGLE_CHARACTER_TOKENS['}'], '}', None), 0)),
    (',', (Token(SINGLE_CHARACTER_TOKENS[','], ',', None), 0)),
    ('.', (Token(SINGLE_CHARACTER_TOKENS['.'], '.', None), 0)),
    ('-', (Token(SINGLE_CHARACTER_TOKENS['-'], '-', None), 0)),
    ('+', (Token(SINGLE_CHARACTER_TOKENS['+'], '+', None), 0)),
    (';', (Token(SINGLE_CHARACTER_TOKENS[';'], ';', None), 0)),
    ('*', (Token(SINGLE_CHARACTER_TOKENS['*'], '*', None), 0)),
])
def test_single_character_tokens(source_code, expected):
    assert single_character_tokens(source_code) == expected
    



def single_character_tokens(source_code):
    return (Token(SINGLE_CHARACTER_TOKENS[source_code[0]], source_code[0], None), 0)
