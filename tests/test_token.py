"""
We want a token class that we can use to represent
the tokens that we find in the source code. 
"""

from plox.token import Token
from plox.tokentype import TokenType

def test_token_creation():
    """
    We need to be able to create tokens.

    The tokens need to have
    
    type
       this is the tokentype enum. We use this
       to determine which type of token it is.

    lexeme
       The string that was matched

    literal
       The actual value of the token. This is
       usually null for most tokens, but for
       things like strings and numbers, we need
       to store the actual value.

    line number
       The line number where the token was found.
       I think this is used for error reporting.
    """
    token = Token(TokenType.LEFT_PAREN, "(", None, 1)
    
    assert token.type == TokenType.LEFT_PAREN
    assert token.lexeme == "("
    assert token.literal is None
    assert token.line == 1

def test_token_equality():
    """
    I suppose we don't super need this.
    """
    token1 = Token(TokenType.LEFT_PAREN, "(", None, 1)
    token2 = Token(TokenType.LEFT_PAREN, "(", None, 1)

    assert token1 == token2

def test_to_string():
    """
    We want a string representation for logging
    and general verification purposes. We might not
    need this later.
    """
    token = Token(TokenType.LEFT_PAREN, "(", None, 1)

    assert str(token) == "Token(type=<TokenType.LEFT_PAREN: 1>, lexeme='(', literal=None, line=1)"