import ply.yacc as yacc
from lexer import lexer, tokens

def p_start(p):
    'start : structures'
    p[0] = p[1]

def p_structures(p):
    '''structures : structures structure
                  | structure'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_structure(p):
    '''structure : var_decl
                 | func_decl
                 | for_decl
                 | if_decl
                 | statement'''
    p[0] = p[1]

def p_var_decl(p):
    'var_decl : VAR TYPE IDENTIFIER EQUAL value SEMICOLON'
    p[0] = {'type': 'var_decl', 'var_type': p[2], 'identifier': p[3], 'value': p[5]}
    
    if p[2] == "ent" and not isinstance(p[5], int):
        raise SyntaxError(f"Error de tipo: se esperaba un entero, se obtuvo {p[5]}")
    elif p[2] == "flot" and not isinstance(p[5], float):
        raise SyntaxError(f"Error de tipo: se esperaba un flotante, se obtuvo {p[5]}")
    elif p[2] == "cad" and not (p[5].startswith('"') and p[5].endswith('"')):
        raise SyntaxError(f"Error de tipo: se esperaba una cadena, se obtuvo {p[5]}")
    elif p[2] == "car" and not (p[5].startswith("'") and p[5].endswith("'") and len(p[5]) == 3):
        raise SyntaxError(f"Error de tipo: se esperaba un caracter, se obtuvo {p[5]}")
    elif p[2] == "bool":
        if p[5] != 'verdadero' and p[5] != 'falso':
            raise SyntaxError(f"Error de tipo: se esperaba un boolean, se obtuvo {p[5]}")

def p_func_decl(p):
    'func_decl : FUNC IDENTIFIER LPAREN RPAREN LBRACKET statements RBRACKET'
    p[0] = {'type': 'func_decl', 'name': p[2], 'body': p[6]}
    print(f"func: {p[6]}")

def p_for_decl(p):
    'for_decl : FOR LPAREN var_decl condition SEMICOLON increment RPAREN LBRACKET statements RBRACKET'
    p[0] = {'type': 'for_decl', 'init': p[3], 'cond': p[4], 'inc': p[6], 'body': p[9]}

def p_if_decl(p):
    'if_decl : IF LPAREN condition RPAREN LBRACKET statements RBRACKET else_decl'
    p[0] = {'type': 'if_decl', 'condition': p[3], 'body': p[6], 'else': p[8]}

def p_else_decl(p):
    'else_decl : ELSE LBRACKET statements RBRACKET'
    p[0] = {'type': 'else_decl', 'body': p[3]}

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_print(p):
    '''statement : PRINT LPAREN STRING RPAREN SEMICOLON
                 | PRINT LPAREN IDENTIFIER RPAREN SEMICOLON'''
    p[0] = {'type': 'print_stmt', 'value': p[3]}

def p_value(p):
    '''value : INT
             | FLOAT
             | BOOLEAN
             | STRING
             | CHAR'''
    p[0] = p[1]

def p_condition(p):
    '''condition : IDENTIFIER OPERATOR value
                 | IDENTIFIER OPERATOR IDENTIFIER'''
    p[0] = ('condition', p[1], p[2], p[3])

def p_increment(p):
    'increment : IDENTIFIER PM'
    p[0] = ('increment', p[1], p[2])

def p_error(p):
    if p:
        raise Exception(f"Syntax error at token {p.type} ('{p.value}') at position {p.lexpos}")
    else:
        raise Exception("Syntax error at EOF")

parser = yacc.yacc()

def parse(data):
    lexer.input(data)
    result = parser.parse(lexer=lexer)
    return result