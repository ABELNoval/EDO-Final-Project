import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def euler_method(f, x0, y0, xf, h):
    n_steps = int((xf - x0) / h) + 1
    x_values = np.linspace(x0, xf, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0

    for i in range(1, n_steps):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])

    return x_values, y_values


def solve_edo():
    try:
        # Obtener valores de entrada del usuario
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        xf = float(entry_xf.get())
        h = float(entry_h.get())

        # Parseo de la función ingresada
        func_str = entry_func.get()
        func = lambda x, y: eval(func_str)

        # Resolver la EDO usando el método de Euler
        x_values, y_values = euler_method(func, x0, y0, xf, h)

        # Graficar el resultado
        plt.plot(x_values, y_values, label="Aproximación con Euler", marker="o")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.title("Método de Euler para EDO")
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Crear la ventana principal
root = tk.Tk()
root.title("Método de Euler para EDO")

# Configurar la expansión en filas y columnas
root.columnconfigure(1, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

# Etiquetas y campos de entrada
tk.Label(root, text="Ecuación diferencial (en términos de x e y):").grid(
    row=0, column=0, sticky="e"
)
entry_func = tk.Entry(root, width=30)
entry_func.grid(row=0, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="x0 (valor inicial de x):").grid(row=1, column=0, sticky="e")
entry_x0 = tk.Entry(root, width=10)
entry_x0.grid(row=1, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="y0 (valor inicial de y):").grid(row=2, column=0, sticky="e")
entry_y0 = tk.Entry(root, width=10)
entry_y0.grid(row=2, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="xf (valor final de x):").grid(row=3, column=0, sticky="e")
entry_xf = tk.Entry(root, width=10)
entry_xf.grid(row=3, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="h (tamaño del paso):").grid(row=4, column=0, sticky="e")
entry_h = tk.Entry(root, width=10)
entry_h.grid(row=4, column=1, padx=10, pady=5, sticky="we")

# Botón para resolver la EDO
btn_solve = tk.Button(root, text="Resolver EDO", command=solve_edo)
btn_solve.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

root.mainloop()
