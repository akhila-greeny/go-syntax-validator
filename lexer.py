import ply.lex as lex

tokens = (
    'VAR', 'CONST', 'FUNC', 'TYPE', 'STRUCT', 'RETURN',
    'IF', 'ELSE', 'FOR',
    'INTTYPE', 'STRINGTYPE',
    'ID', 'NUMBER',
    'DECLARE', 'ASSIGN',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'GT', 'EQ', 'GE', 'LE', 'NE',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'SEMI', 'COMMA',
    'LBRACKET', 'RBRACKET',
    'COLON'
)

# --------------------
# Operators (longer first)
# --------------------
t_DECLARE = r':='
t_EQ      = r'=='
t_GE      = r'>='
t_LE      = r'<='
t_NE      = r'!='
t_ASSIGN  = r'='
t_LT      = r'<'
t_GT      = r'>'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

# --------------------
# Delimiters
# --------------------
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMI     = r';'
t_COMMA    = r','
t_COLON    = r':'

# --------------------
# Reserved words
# --------------------
reserved = {
    'var': 'VAR',
    'const': 'CONST',
    'func': 'FUNC',
    'type': 'TYPE',
    'struct': 'STRUCT',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'int': 'INTTYPE',
    'string': 'STRINGTYPE'
}

# --------------------
# Identifiers
# --------------------
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# --------------------
# Numbers
# --------------------
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# --------------------
# Ignored characters
# --------------------
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()