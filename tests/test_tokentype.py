from plox.tokentype import TokenType

def test_tokentype_has_desired_types():
    assert {
        
        # Single-character tokens.
        TokenType.LEFT_PAREN,
        TokenType.RIGHT_PAREN,
        TokenType.LEFT_BRACE,
        TokenType.RIGHT_BRACE,
        TokenType.COMMA,

        TokenType.DOT,
        TokenType.MINUS,
        TokenType.PLUS,
        TokenType.SEMICOLON,
        TokenType.SLASH,
        TokenType.STAR,

        #One or two character tokens
        TokenType.BANG,
        TokenType.BANG_EQUAL,
        TokenType.EQUAL,
        TokenType.EQUAL_EQUAL,
        TokenType.GREATER,
        TokenType.GREATER_EQUAL,
        TokenType.LESS,
        TokenType.LESS_EQUAL,

        # Literals
        TokenType.IDENTIFIER,
        TokenType.STRING,
        TokenType.NUMBER,
        
        # Keywords
        TokenType.AND,
        TokenType.CLASS,
        TokenType.ELSE,
        TokenType.FALSE,
        TokenType.FUN,
        TokenType.FOR,
        TokenType.IF,
        TokenType.NIL,
        TokenType.OR,
        TokenType.PRINT,
        TokenType.RETURN,
        TokenType.SUPER,
        TokenType.THIS,
        TokenType.TRUE,
        TokenType.VAR,
        TokenType.WHILE,
        
        TokenType.EOF,

    } == set(TokenType)