from plox.scanner import Scanner
from plox.token import Token
from plox.tokentype import TokenType

def test_scanner_empty_source():
    scanner = Scanner('')
    assert scanner.tokenize() == []

def test_scanner_single_paren():
    scanner = Scanner('(')
    assert scanner.tokenize() == [Token(TokenType.LEFT_PAREN, '(', None, 1)]

def test_scanner_multiple_parens():
    scanner = Scanner('()')
    expected_tokens = [
        Token(TokenType.LEFT_PAREN, '(', None, 1),
        Token(TokenType.RIGHT_PAREN, ')', None, 2),
    ]
    assert scanner.tokenize() == expected_tokens
