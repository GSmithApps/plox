from dataclasses import dataclass
from typing import Any
from plox_tokentype import TokenType

@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: Any
    line: int
