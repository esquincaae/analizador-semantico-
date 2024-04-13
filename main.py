from yacc import parser, parse
from lexer import lexer
#import interpreter

def execute_parser(script):
    result = []
    sintact = parse(script)
    if sintact != None:
        try:
            parser.parse(script)
            print("Análisis sintáctico completado sin errores. Mostrando tokens:")
            lexer.input(script)
            for tok in lexer:
                result.append((tok.type,tok.value))
        except Exception as e:
            print(f"Error al analizar la entrada: {e}")
        return result    
    else:
        return f"error de sintaxis"

def execute_python(script):
    #antes del return se llama al interpreter
    return f"print('{script}')"