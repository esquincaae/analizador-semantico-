import ply.lex as lex

tokens = [
    'VAR', 'TYPE', 'EQUAL', 'SEMICOLON',
    'INT', 'FLOAT', 'BOOLEAN', 'STRING', 'CHAR',
    'FUNC', 'FOR', 'PRINT', 'IF', 'ELSE',
    'LBRACKET', 'RBRACKET', 'LPAREN', 'RPAREN',
    'OPERATOR', 'PM', 'IDENTIFIER'
]

t_VAR = r'\bvar\b'
t_FUNC = r'\bfunc\b'
t_FOR = r'\bfor\b'
t_PRINT = r'\bprint\b'
t_IF = r'\bif\b'
t_ELSE = r'\belse\b'
t_TYPE = r'\b(ent|flot|bool|cad|car)\b'

t_EQUAL = r'='
t_SEMICOLON = r';'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_OPERATOR = r'\<=|>=|!=|==|<|>'
t_PM = r'\+\+|--'


def t_STRING(t):
    r'"([^;()\[\]{}]|\\")*"'
    #t.value = t.value[1:-1]  # Elimina las comillas dobles al principio y al final del string
    return t


def t_CHAR(t):
    r"\'([^'\\]|\\.)\'"
    #t.value = t.value[1:-1]  # Elimina las comillas
    return t

def t_BOOLEAN(t):
    r'\bverdadero\b|\bfalso\b'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
        'var': 'VAR', 'func': 'FUNC', 'Para': 'FOR', 
        'si': 'IF', 'sino': 'ELSE', 'ent': 'TYPE', 'flot': 'TYPE', 
        'bool': 'TYPE', 'cad': 'TYPE', 'car': 'TYPE', 'verdadero': 'BOOLEAN', 
        'falso': 'BOOLEAN', 'imprimir': 'PRINT'
    }
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

