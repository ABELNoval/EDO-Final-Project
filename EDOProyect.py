import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import math


# Función que implementa el Método de Euler
def euler_method(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(1, n + 1):
        x = x_values[-1]
        y = y_values[-1]
        y_new = y + h * f(x, y)  # Método de Euler: y(i+1) = y(i) + h*f(x(i), y(i))
        x_new = x + h

        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values


# Función que convierte la ecuación ingresada en una función de Python
def create_function(edo_str):
    try:
        # Reemplazar los operadores de la ecuación de texto para hacerla ejecutable
        # En este caso, 'diff(y,x)' es equivalente a 'y'
        edo_str = edo_str.replace("diff(y,x)", "y")
        edo_str = edo_str.replace("x", "x")  # Asegúrate de que 'x' se reconozca
        edo_str = edo_str.replace("y", "y")  # Asegúrate de que 'y' se reconozca
        edo_str = edo_str.replace("sin", "math.sin")
        edo_str = edo_str.replace("cos", "math.cos")
        edo_str = edo_str.replace("tan", "math.tan")
        edo_str = edo_str.replace(
            "log", "math.log"
        )  # log se refiere al logaritmo natural en math
        edo_str = edo_str.replace(
            "ln", "math.log"
        )  # ln también se refiere al logaritmo natural en math
        edo_str = edo_str.replace(
            "e", "math.e"
        )  # Reemplazar 'e' por la constante math.e
        edo_str = edo_str.replace("exp", "math.exp")

        # Evaluar la ecuación como una función
        def f(x, y):
            return eval(
                edo_str
            )  # Usamos eval para evaluar la ecuación como una función en x y y

        return f
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al interpretar la EDO: {e}")
        return None


# Función que se ejecuta al hacer clic en "Resolver"
def solve():
    edo_str = edo_entry.get()  # Obtener la ecuación ingresada
    x0 = float(x0_entry.get())  # Obtener el valor de x0
    y0 = float(y0_entry.get())  # Obtener el valor de y0
    h = float(h_entry.get())  # Obtener el valor de h
    n = int(n_entry.get())  # Obtener el número de pasos

    # Crear la función que representa la EDO
    f = create_function(edo_str)

    if f is not None:
        # Resolver la EDO con el método de Euler
        x_values, y_values = euler_method(f, x0, y0, h, n)

        # Graficar la solución
        plt.plot(x_values, y_values, marker="o", color="b", label="Método de Euler")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Solución de la EDO usando el Método de Euler")
        plt.grid(True)
        plt.legend()
        plt.show()


# Función para mostrar el mensaje de ayuda
def show_help():
    help_message = (
        "Este programa resuelve ecuaciones diferenciales de la forma 'y' = f(x, y)\n\n"
        "1. Introduzca la ecuación diferencial en la caja de texto 'Ecuación diferencial'\n"
        "   Ejemplo: 'diff(y,x) - (x + y/5)'\n"
        "2. Ingrese los valores de x0, y0, h y n para resolver la ecuación.\n"
        "3. Haga clic en 'Resolver' para ver la solución y la gráfica."
    )
    messagebox.showinfo("Ayuda", help_message)


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Método de Euler para EDOs")

# Establecer el tamaño de la ventana
root.geometry("500x350")

# Etiquetas y campos de entrada para los parámetros
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Ecuación diferencial (como 'y' = ...')").grid(
    row=0, column=0, sticky="e", padx=5, pady=5
)
edo_entry = tk.Entry(frame, width=50)
edo_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="x0 (Valor inicial de x)").grid(
    row=1, column=0, sticky="e", padx=5, pady=5
)
x0_entry = tk.Entry(frame)
x0_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="y0 (Valor inicial de y)").grid(
    row=2, column=0, sticky="e", padx=5, pady=5
)
y0_entry = tk.Entry(frame)
y0_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="h (Paso de integración)").grid(
    row=3, column=0, sticky="e", padx=5, pady=5
)
h_entry = tk.Entry(frame)
h_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="n (Número de pasos)").grid(
    row=4, column=0, sticky="e", padx=5, pady=5
)
n_entry = tk.Entry(frame)
n_entry.grid(row=4, column=1, padx=5, pady=5)

# Botones para resolver y mostrar ayuda
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

solve_button = tk.Button(button_frame, text="Resolver", command=solve, width=20)
solve_button.grid(row=0, column=0, padx=10)

help_button = tk.Button(button_frame, text="Ayuda", command=show_help, width=20)
help_button.grid(row=0, column=1, padx=10)

# Botón para salir
exit_button = tk.Button(root, text="Salir", command=root.quit, width=20)
exit_button.pack(pady=10)

# Ejecutar la interfaz
root.mainloop()
