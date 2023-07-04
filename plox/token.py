"""
We want two types of token classes. One with
a line number, and one without a line number. 
On the one with a line number, we'll just
have a token without a line number, and then
add a line number to it. The
required fields for the token are:

type: TokenType
   this is the tokentype enum. We use this
   to determine which type of token it is.

lexeme: str
   The string that was matched

literal: Any
   The actual value of the token. This is
   usually null for most tokens, but for
   things like strings and numbers, we need
   to store the actual value.

And for the token with line, we will have
a token and a line number, like this

token: Token
   The token as defined above

line number: int
   The line number where the token was found.
   I think this is used for error reporting.

Methods
-------   

We simply need to be able to convert these
to strings.

"""

from dataclasses import dataclass
from typing import Any
from .tokentype import TokenType

def test_token_creation():

   token = Token(TokenType.LEFT_PAREN, "(", None)
   
   assert token.type == TokenType.LEFT_PAREN
   assert token.lexeme == "("
   assert token.literal is None

def test_to_string():

   token = Token(TokenType.LEFT_PAREN, "(", None)

   assert str(token) == "Token(type=<TokenType.LEFT_PAREN: 1>, lexeme='(', literal=None)"

def test_token_with_line_creation():

   token = Token(TokenType.LEFT_PAREN, "(", None)
   token_with_line = TokenWithLine(token, 1)

   assert token_with_line.token == token
   assert token_with_line.line == 1

def test_token_with_line_to_string():
   
   token = Token(TokenType.LEFT_PAREN, "(", None)
   token_with_line = TokenWithLine(token, 1)

   assert str(token_with_line) == "TokenWithLine(token=Token(type=<TokenType.LEFT_PAREN: 1>, lexeme='(', literal=None), line=1)"

@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: Any

@dataclass
class TokenWithLine:
    token: Token
    line: int
