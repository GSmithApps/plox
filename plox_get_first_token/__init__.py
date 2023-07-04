from plox_get_first_token import get_first_token
from plox_token import Token
from plox_tokentype import TokenType

def test_get_first_token_empty_string():
    assert get_first_token('') is None

def test_get_first_token_single_left_paren():
    assert get_first_token('(') == Token(TokenType.LEFT_PAREN, '(', None, 1)

def test_get_first_token_single_right_paren():
    assert get_first_token(')') == Token(TokenType.RIGHT_PAREN, ')', None, 1)

def test_get_first_token_multiple_tokens():
    assert get_first_token('()') == Token(TokenType.LEFT_PAREN, '(', None, 1)


def get_first_token(text):
    pass