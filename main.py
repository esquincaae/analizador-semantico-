from yacc import parser, parse
from lexer import lexer
#import interpreter

def execute_parser(script):
    try:
        # Analizar el script usando el parser definido
        result = parse(script)
        if result is not None:
            tokens = "Análisis sintáctico completado sin errores. Mostrando tokens:\n"
            # Inicializar el lexer con el script para extraer y mostrar los tokens
            lexer.input(script)
            tokens = [(tok.type, ":",tok.value) for tok in lexer]
            return tokens
            #print(tokens)
        else:
            # Devolver un mensaje de error si el resultado del análisis es None
            return "Error de sintaxis: el parser no pudo procesar la entrada correctamente."
    except Exception as e:
        # Manejar cualquier excepción que ocurra durante el análisis
        print(f"Error al analizar la entrada: {e}")
        return []
    
#script = f"var car letra = 'a';"
#execute_parser(script)

def execute_python(script):
    #antes del return se llama al interpreter
    return f"print('{script}')"