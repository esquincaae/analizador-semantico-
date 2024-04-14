from yacc import parse
from lexer import lexer
from interpreter import Interpreter

def execute_parser(script):
    try:
        result = parse(script)
        if result is not None:
            print("Análisis sintáctico completado sin errores. Mostrando tokens:\n")
            lexer.input(script)
            tokens = [(tok.type, ":",tok.value) for tok in lexer]
            return tokens
        else:
            return "Error de sintaxis: el parser no pudo procesar la entrada correctamente."
    except Exception as e:
        print(f"Error al analizar la entrada: {e}")
        return []

def execute_python(script):
    parse_result = parse(script)
    interpreter = Interpreter()
    output_obj = interpreter.execute(parse_result)
    print(output_obj.output.strip())
    if isinstance(output_obj.output, str):  # Verificar que es un string
        exec(output_obj.output)
    else:
        print("El código generado no es un string:", type(output_obj.output))
    return output_obj.output
