import tkinter as tk
from tkinter import messagebox
from main import execute_parser, execute_python
import interpreter

def procesar():
    interpreter.variables = []
    interpreter.value_variable = []
    interpreter.func = []
    interpreter.for_out = []
    interpreter.out_pps = ""
    entrada = text_area_entrada.get('1.0', tk.END).strip()  # Obtener y limpiar la entrada
    if not entrada:
        messagebox.showerror("Error", "La entrada no puede estar vacía.")
        return

    # Mostrar el resultado del análisis léxico/sintáctico
    text_area_lexico.delete('1.0', tk.END)
    resultado_parser = execute_parser(entrada)
    text_area_lexico.insert(tk.END, resultado_parser)

    try:
        text_area_python.delete('1.0', tk.END)
        codigo_python = execute_python(entrada)
        print(codigo_python)
        text_area_python.insert(tk.END, codigo_python)

        messagebox.showinfo("Éxito", "Script procesado y ejecutado.")
    except Exception as e:
        messagebox.showerror("Error de ejecución", str(e))

# Configuración de la GUI (esto permanece igual)
root = tk.Tk()
root.title("Lyra: Analizador semántico")
label_entrada = tk.Label(root, text="Entrada en Lyra")
label_entrada.pack()
text_area_entrada = tk.Text(root, height=10, width=100)
text_area_entrada.pack(padx=10, pady=10)

boton_procesar = tk.Button(root, text="PROCESAR", command=procesar)
boton_procesar.pack(padx=10, pady=10)

label_lexico = tk.Label(root, text="Salida sintáctica/léxica")
label_lexico.pack()
text_area_lexico = tk.Text(root, height=10, width=100)
text_area_lexico.pack(padx=10, pady=10)

label_python = tk.Label(root, text="Salida en Python")
label_python.pack()
text_area_python = tk.Text(root, height=10, width=100)
text_area_python.pack(padx=10, pady=10)

root.mainloop()