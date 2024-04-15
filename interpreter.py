for_out = []
variables = []
value_variable = []
out_pps = ""
func = []

def generate_code(parsers):
    global out_pps
    print(parsers)
    for parser in parsers:
        print(parser['type'])
        if parser['type'] == 'for_decl':
            if parser['init']['identifier'] not in variables:
                variables.append(parser['init']['identifier'])
                value_variable.append(parser['init']['value'])
            else:
                out_pps += f"YA DECLARADA\n"

            for i in range(parser['cond'][3]):
                value_variable[variables.index(parser['init']['identifier'])] += 1
                if parser['body'][0]['value'] in variables:
                    for_out.append(value_variable[variables.index(parser['body'][0]['value'])])
                else:
                    for_out.append(parser['body'][0]['value'])
            return for_out
        elif parser['type'] == 'print_stmt':
            print("Entre al print")
            if parser['value'] in variables:
                out_pps += f"{value_variable[variables.index(parser['value'])]}\n"
            else:
                out_pps += f"{parser['value']}\n"
        elif parser['type'] == 'var_decl':
            if parser['identifier'] not in variables:
                if parser['var_type'] == 'ent':
                    if isinstance(parser['value'], int):
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"Error de tipo: se esperaba un entero, se obtuvo {parser['value']}\n"

                elif parser['var_type'] == 'flot':
                    if isinstance(parser['value'], float):
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"Error de tipo: se esperaba un flotante, se obtuvo {parser['value']}\n"

                elif parser['var_type'] == 'cad':
                    if parser['value'].startswith('"') and parser['value'].endswith('"'):
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"Error de tipo: se esperaba una cadena, se obtuvo {parser['value']}\n"

                elif parser['var_type'] == 'car':
                    if parser['value'].startswith("'") and parser['value'].endswith("'") and len(
                            parser['value']) == 3:
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"Error de tipo: se esperaba un caracter, se obtuvo {parser['value']}\n"

                elif parser['var_type'] == 'bool':
                    if parser['value'] == 'verdadero' or parser['value'] == 'falso':
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"Error de tipo: se esperaba un boolean, se obtuvo {parser['value']}\n"

                else:
                    out_pps += f"Error de tipo: tipo de variable no reconocido\n"

            else:
                out_pps += f"YA DECLARADA\n"

        elif parser['type'] == 'if_decl':
            if parser['condition'][1] in variables:
                validation = f"{value_variable[variables.index(parser['condition'][1])]} {parser['condition'][2]} {parser['condition'][-1]}"
                if eval(validation):
                    generate_code(parser['body'])
                else:
                    generate_code(parser['else']['body'])
            elif parser['condition'][-1] in variables:
                validation = f"{parser['condition'][1]} {parser['condition'][2]} {value_variable[variables.index(parser['condition'][-1])]}"
                if eval(validation):
                    generate_code(parser['body'])
                else:
                    generate_code(parser['else']['body'])
            elif parser['condition'][1] in variables and parser['condition'][-1] in variables:
                validation = f"{value_variable[variables.index(parser['condition'][1])]} {parser['condition'][2]} {value_variable[variables.index(parser['condition'][-1])]}"
                if eval(validation):
                    generate_code(parser['body'])
                else:
                    generate_code(parser['else']['body'])
        elif parser['type'] == 'func_decl':
            if parser['name'] not in func:
                func.append(parser['name'])
                generate_code(parser['body'])
            else:
                out_pps += f"YA DECLARADA\n"
    return out_pps