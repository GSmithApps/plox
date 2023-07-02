from dataclasses import dataclass
from typing import Any
from plox.tokentype import TokenType

@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: Any
    line: int
