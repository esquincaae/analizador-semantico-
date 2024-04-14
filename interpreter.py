class Interpreter:
    def __init__(self):
        self.output = InterpreterOutput()

    def analyze_var_decl(self, var_decl):
        self.output.add_variable(var_decl['identifier'], var_decl['value'], var_decl['var_type'])

    def analyze_condition(self, cond):
        if len(cond) == 4:
            _, left, operator, right = cond
            return f"{left} {operator} {right}"
        else:
            raise ValueError("Condición del bucle for no válida: debe ser una tupla de cuatro elementos")

    def analyze_increment(self, inc):
        # Asume que el incremento es una tupla como ('i', '++')
        if len(inc) == 3:
            _, identifier, op = inc
            if op == '++':
                return f"{identifier} += 1"
            elif op == '--':
                return f"{identifier} -= 1"
        else:
            raise ValueError("Incremento del bucle for no válido: debe ser una tupla de tres elementos")

    def analyze_for_decl(self, for_decl):
        init = self.analyze_var_decl(for_decl['init']) if for_decl['init'].get('type') == 'var_decl' else ""
        cond = self.analyze_condition(for_decl['cond'])
        inc = self.analyze_increment(for_decl['inc'])
        body_statements = [self.execute_statement(stmt) for stmt in for_decl['body']]
        body = '\n    '.join(filter(None, body_statements))
        #
        #
        loop = f"{init}\nwhile {cond}:\n    {inc}\n    {body}"
        self.output.add_code(loop)

    def analyze_func_decl(self, func_decl):
        func_name = func_decl['name']
        # Asumimos que no hay parámetros, simplificando el manejo de la llamada
        body_statements = [self.execute_statement(stmt) for stmt in func_decl['body']]
        body = '\n    '.join(filter(None, body_statements))
        if body.strip():  # Si el cuerpo está vacío, inserta 'pass' para asegurar una función válida
            body = "pass"
        func_def = f"def {func_name}():\n    {body}\n"
        func_call = f"{func_name}()"  # Genera la llamada a la función
        # Añade la definición de la función y la llamada a la salida
        self.output.add_code(func_def + func_call + '\n')

    def analyze_if_decl(self, if_decl):
        condition = self.analyze_condition(if_decl['condition'])
        body_statements = [self.execute_statement(stmt) for stmt in if_decl['body']]
        body = '\n    '.join(filter(None, body_statements))
        if_body = f"if {condition}:\n    {body}"
        
        if if_decl['else']:
            else_body = self.analyze_else_decl(if_decl['else'])
            if_body += else_body
        
        self.output.add_code(if_body)

    def analyze_else_decl(self, else_decl):
        if else_decl is None:
            return ""
        body_statements = [self.execute_statement(stmt) for stmt in else_decl['body']]
        body = '\n    '.join(filter(None, body_statements))
        return f"\nelse:\n    {body}"

    def analyze_print(self, print_stmt):
        # El argumento print_stmt contiene el valor a imprimir
        value = print_stmt['value']
        # Añade la instrucción de impresión al output del código
        self.output.add_print(value)

    def execute_statement(self, stmt):
        if stmt['type'] == 'var_decl':
            return self.analyze_var_decl(stmt)
        elif stmt['type'] == 'print_stmt':
            self.analyze_print(stmt)
            return ""
        elif stmt['type'] == 'if_decl':
            self.analyze_if_decl(stmt)
            return ""
        elif stmt['type'] == 'else_decl':
            self.analyze_else_decl(stmt)
        return ""

    def execute(self, parse_output):
        for node in parse_output:
            if node['type'] == 'var_decl':
                self.analyze_var_decl(node)
            elif node['type'] == 'print_stmt':
                self.analyze_print(node)
            elif node['type'] == 'for_decl':
                self.analyze_for_decl(node)
            elif node['type'] == 'func_decl':
                self.analyze_func_decl(node)
            elif node['type'] == 'if_decl':
                self.analyze_if_decl(node)
            elif node['type'] == 'else_decl':
                self.analyze_else_decl(node)
        return self.output




class InterpreterOutput:
    def __init__(self):
        self.variables = {}
        self.output = ""

    def add_variable(self, name, value, var_type):
        self.variables[name] = {'type': var_type, 'value': value}
        self.output += f"{name} = {value}\n"

    def add_print(self, value):
        self.output += f"print({value})\n"


    def add_code(self, code):
        self.output += code + "\n"
