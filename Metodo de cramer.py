from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import numpy as np

def validar_datos():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "Algebra" and contraseña == "Proyecto":
        messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido de nuevo!")
        ventana.destroy()
    else:
        messagebox.showerror("Error de inicio de sesión", "Introduzca los datos correctos")

def salir():
    ventana.destroy()

def mostrar_desarrolladores():
    ventana_desarrolladores = Toplevel()
    ventana_desarrolladores.title("Desarrolladores")
    ventana_desarrolladores.geometry("400x300")

    label_titulo = Label(ventana_desarrolladores, text="Desarrolladores", font=("Dark Mono", 14, "bold"))
    label_titulo.pack(pady=10)

    label_nombres = Label(ventana_desarrolladores, text="1. Jonathan Raul Cruz Magaña\n2. Juan Josmar Bacelis de la Rosa\n3. Patricia Beatriz Perez Berdejo\n4. Juan Maximiliano Hernandez Martin\n5. Rider Alberto Peraza Ortega", font=("Dark Mono", 12))
    label_nombres.pack()

def mostrar_instrucciones():
    ventana_instrucciones = Toplevel()
    ventana_instrucciones.title("Instrucciones")
    ventana_instrucciones.geometry("600x400")
    
    label_titulo = Label(ventana_instrucciones, text="Instrucciones", font=("Dark Mono", 14, "bold"))
    label_titulo.pack(pady=10)

    label_nombres = Label(ventana_instrucciones, text="En el siguente programa se utiliza en metodo de cramer\npara resolver sistemas de ecuaciones de 3 constantes \n""\nPasos a seguir\n"" \n1. Al ingresar deberas colocar tu matriz \n2. Colocaras sus determinantes para su realizacion\n3. Abra botones para limpar tu matriz y limpiar tu determinante\n4. Le picaras al boton de resolver\n5. Y veras tu procedimiento y respuesta mediante el metodo de cramer", font=("Dark Mono", 12))
    label_nombres.pack()    

# VENTANA DE INICIO DE SESION
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("600x500")
ventana.configure(bg="honeydew")

dark_mono_font = font.Font(family="Dark Mono")

# TITULO
label_bienvenida = Label(ventana, text="Bienvenido", font=(dark_mono_font, 16, "bold"), bg="honeydew")
label_bienvenida.pack(pady=15)

# INSTRUCCION POR DEBAJO DEL TITULO
label_instrucciones = Label(ventana, text="Por favor, ingrese los datos para ingresar", font=(dark_mono_font, 12), bg="honeydew")
label_instrucciones.pack()

# ENTRADAS DE USUARIO Y CONTRASEÑA
label_usuario = Label(ventana, text="Usuario", font=(dark_mono_font, 12), bg="honeydew")
label_usuario.pack(pady=10)
entry_usuario = Entry(ventana, font=(dark_mono_font, 12))
entry_usuario.pack()

label_contraseña = Label(ventana, text="Contraseña", font=(dark_mono_font, 12), bg="honeydew")
label_contraseña.pack(pady=10)
entry_contraseña = Entry(ventana, show="*", font=(dark_mono_font, 12))
entry_contraseña.pack()

# BOTON DE INICIO DE SESION
boton_ingresar = Button(ventana, text="Ingresar", command=validar_datos, font=(dark_mono_font, 12))
boton_ingresar.pack(pady=15)

# BOTON PARA SALIR
boton_salir = Button(ventana, text="Salir", command=salir, font=(dark_mono_font, 12))
boton_salir.pack(pady=5)

# BOTON PARA ENTRAR A DESARROLLADORES
boton_desarrolladores = Button(ventana, text="Desarrolladores", command=mostrar_desarrolladores, font=(dark_mono_font, 12))
boton_desarrolladores.pack(pady=5)

# BOTON PARA ENTRAR A LAS INSTRUCCIONES
boton_instrucciones = Button(ventana, text="Instrucciones", command=mostrar_instrucciones, font=(dark_mono_font, 12))
boton_instrucciones.pack(pady=5)

# EJECUCION DEL INICIO DE SESION
ventana.mainloop()

def solve_equation():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            value = entries[i][j].get()
            if not value:
                messagebox.showerror("Error", "Debe ingresar todos los valores de la matriz.")
                return
            try:
                row.append(float(value))
            except ValueError:
                messagebox.showerror("Error", "Debe ingresar valores numéricos en la matriz.")
                return
        matrix.append(row)
    
    determinant = np.linalg.det(matrix)
    
    if determinant == 0:
        result_label.config(text="El determinante es cero. No se puede resolver el sistema.")
    else:
        constants = []
        for i in range(3):
            value = constants_entries[i].get()
            if not value:
                messagebox.showerror("Error", "Debe ingresar todos los valores de las constantes.")
                return
            try:
                constants.append(float(value))
            except ValueError:
                messagebox.showerror("Error", "Debe ingresar valores numéricos en las constantes.")
                return
        
        result_matrix = []
        steps = []
        for i in range(3):
            temp_matrix = np.copy(matrix)
            temp_matrix[:, i] = constants
            solution = np.linalg.det(temp_matrix) / determinant
            result_matrix.append(solution)
            
            step = "Paso {}: ".format(i+1)
            step += "Reemplazar columna {} con constantes: \n\n{}\n".format(i+1, temp_matrix)
            step += "Determinante del sistema:\n\n{}\n".format(round(np.linalg.det(temp_matrix), 2))
            step += "Determinante principal:\n\n{}\n".format(round(determinant, 2))
            step += "Solución para x{}: {}\n\n".format(i+1, round(solution, 2))
            steps.append(step)
        
        result_label.config(text="Soluciones:\n\nx = {:.2f}\ny = {:.2f}\nz = {:.2f}\n\n{}".format(*result_matrix, '\n'.join(steps)))

def clear_matrix():
    for i in range(3):
        for j in range(3):
            entries[i][j].delete(0, tk.END)
    for i in range(3):
        constants_entries[i].delete(0, tk.END)
    result_label.config(text="")

def create_new_matrix():
    for i in range(3):
        for j in range(3):
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(state=tk.NORMAL)
        constants_entries[i].delete(0, tk.END)
        constants_entries[i].config(state=tk.NORMAL)
    result_label.config(text="")

def clear_entries():
    for i in range(3):
        for j in range(3):
            entries[i][j].delete(0, tk.END)

def clear_constants():
    for i in range(3):
        constants_entries[i].delete(0, tk.END)

# Crear la ventana principal
window = tk.Tk()
window.title("Resolución de sistema de ecuaciones")


# Obtener el ancho y alto de la ventana
window_width = 600
window_height = 400

# Obtener el ancho y alto de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Establecer la posición de la ventana
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Crear el marco con barra de desplazamiento
canvas = tk.Canvas(window)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Añadir barra de desplazamiento
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Crear el marco interno
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Crear el subtítulo
subtitle_label = tk.Label(frame, text="Ingrese la matriz y sus constantes")
subtitle_label.grid(row=0, columnspan=3, padx=5, pady=10)

# Crear las cajas de entrada
entries = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(frame, width=8)
        entry.grid(row=i+1, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

# Crear las etiquetas para las constantes
constants_entries = []
constants_label = tk.Label(frame, text="Constantes:")
constants_label.grid(row=1, column=4, padx=5, pady=5)
for i in range(3):
    entry = tk.Entry(frame, width=8)
    entry.grid(row=i+1, column=5, padx=5, pady=5)
    constants_entries.append(entry)

# Crear los botones
solve_button = tk.Button(frame, text="Resolver", command=solve_equation)
solve_button.grid(row=4, column=2, padx=5, pady=10)

clear_entries_button = tk.Button(frame, text="Limpiar matriz", command=clear_entries)
clear_entries_button.grid(row=4, column=5, padx=5, pady=10)

clear_constants_button = tk.Button(frame, text="Limpiar constantes", command=clear_constants)
clear_constants_button.grid(row=4, column=6, padx=5, pady=10)

# Crear la etiqueta de resultado
result_label = tk.Label(frame, text="")
result_label.grid(row=5, columnspan=3, padx=5, pady=10)

# Configurar el desplazamiento del lienzo al desplazar la barra
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Configurar el desplazamiento del lienzo al desplazar con el mouse
frame.bind("<Enter>", lambda e: canvas.unbind_all("<MouseWheel>"))
frame.bind("<Leave>", lambda e: canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units")))

# Ejecutar la aplicación
window.mainloop()
