import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk


def euler_method(f, x0, y0, xf, h):
    n_steps = int((xf - x0) / h) + 1
    x_values = np.linspace(x0, xf, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0

    for i in range(1, n_steps):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])

    return x_values, y_values


def validate_and_correct(x0, y0, xf, h, func_str):
    messages = []
    corrections = []

    if xf <= x0:
        messages.append(
            "Error: El valor final de x (xf) debe ser mayor que el valor inicial (x0)."
        )
        corrections.append("Ajustando xf a x0 + 1.")
        xf = x0 + 1

    if h <= 0:
        messages.append("Error: El tamaño de paso (h) debe ser positivo.")
        corrections.append("Ajustando h a 0.1.")
        h = 0.1

    try:
        func = lambda x, y: eval(func_str)
        test_val = func(x0, y0)  # Validar que la función sea evaluable
    except Exception as e:
        raise ValueError(f"La función ingresada no es válida: {e}")

    return x0, y0, xf, h, func, messages, corrections


def handle_numerical_issues(func, x0, y0, xf, h):
    report = []
    corrections = []

    if h > (xf - x0) / 10:
        report.append(f"Advertencia: El paso h={h} podría causar inestabilidad.")
        corrections.append(f"Reducimos a h={(xf - x0) / 20:.4f}.")
        h = (xf - x0) / 20

    if abs(xf - x0) > 100 and h < 1e-3:
        report.append(
            "Advertencia: El rango combinado con un paso pequeño (h) podría causar acumulación de errores."
        )
        corrections.append("Ajustando h a un mínimo de 1e-3.")
        h = max(h, 1e-3)

    try:
        test_x = np.linspace(x0, xf, 10)
        test_y = [y0]
        for i in range(1, len(test_x)):
            dydx_prev = func(test_x[i - 1], test_y[-1])
            dydx_curr = func(test_x[i], test_y[-1] + h * dydx_prev)
            if abs(dydx_curr - dydx_prev) > 10:
                report.append(
                    "Advertencia: Se detectó rigidez, cambios rápidos en la derivada."
                )
                corrections.append(
                    "Considere un método más adecuado para EDOs rígidas."
                )
                break
    except Exception as e:
        report.append(f"Problema al evaluar rigidez: {e}")

    try:
        test_points = [(x0 + i * h, y0 + i * h * func(x0, y0)) for i in range(5)]
        for i in range(1, len(test_points)):
            diff = abs(func(*test_points[i]) - func(*test_points[i - 1]))
            if diff > 10:
                report.append("Advertencia: Se detectaron discontinuidades en f(x, y).")
                corrections.append("Revise la función ingresada por posibles errores.")
                break
    except Exception as e:
        report.append(f"No se pudo verificar continuidad: {e}")

    return h, report, corrections


def plot_results(original_x, original_y, corrected_x, corrected_y, messages):
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.plot(original_x, original_y, label="Aproximación Original (Euler)", marker="o")
    plt.title("Solución Original con Problemas Numéricos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", lw=0.5, ls="--")
    plt.axvline(0, color="black", lw=0.5, ls="--")
    plt.legend()

    for msg in messages:
        plt.annotate(
            msg,
            xy=(original_x[-1], original_y[-1]),
            textcoords="offset points",
            xytext=(-10, 10),
            ha="center",
            fontsize=8,
            color="red",
        )

    plt.subplot(1, 2, 2)
    plt.plot(
        corrected_x,
        corrected_y,
        label="Aproximación Corregida",
        marker="o",
        color="orange",
    )
    plt.title("Solución Corregida")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", lw=0.5, ls="--")
    plt.axvline(0, color="black", lw=0.5, ls="--")
    plt.legend()

    plt.tight_layout()
    plt.show()


def solve_edo():
    try:
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        xf = float(entry_xf.get())
        h = float(entry_h.get())
        func_str = entry_func.get()

        x0, y0, xf, h, func, messages, corrections = validate_and_correct(
            x0, y0, xf, h, func_str
        )

        h, additional_report, additional_corrections = handle_numerical_issues(
            func, x0, y0, xf, h
        )

        # Limpiar las áreas de texto
        error_tab.delete(1.0, tk.END)
        error_solution_tab.delete(1.0, tk.END)

        # Si no hay errores, notificar al usuario
        if not messages and not additional_report:
            messagebox.showinfo(
                "Resultado", "No se encontraron errores, la solución es válida."
            )
            error_tab.insert(tk.END, "No se encontraron errores.\n")
            error_solution_tab.insert(tk.END, "No se realizaron correcciones.\n")
        else:
            if messages:
                error_tab.insert(tk.END, "\n".join(messages) + "\n")
            if additional_report:
                error_tab.insert(tk.END, "\n".join(additional_report) + "\n")

            if corrections or additional_corrections:
                error_solution_tab.insert(
                    tk.END, "\n".join(corrections + additional_corrections) + "\n"
                )
            else:
                error_solution_tab.insert(
                    tk.END, "No se realizaron correcciones necesarias.\n"
                )

        original_x_values, original_y_values = euler_method(func, x0, y0, xf, h)
        corrected_x_values, corrected_y_values = euler_method(func, x0, y0, xf, h)

        plot_results(
            original_x_values,
            original_y_values,
            corrected_x_values,
            corrected_y_values,
            messages,
        )

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Crear la ventana principal
root = tk.Tk()
root.title("Método de Euler para EDO")

# Crear el notebook para pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Crear la pestaña de gráficas
graph_frame = ttk.Frame(notebook)
notebook.add(graph_frame, text="Gráficas")

# Crear la pestaña de errores
error_frame = ttk.Frame(notebook)
notebook.add(error_frame, text="Errores")

# Crear un widget de texto para mostrar errores
error_tab = tk.Text(error_frame, wrap=tk.WORD, height=10, width=50)
error_tab.pack(expand=True, fill="both", padx=10, pady=5)

# Crear un widget de texto para mostrar soluciones a los errores
error_solution_tab = tk.Text(error_frame, wrap=tk.WORD, height=10, width=50)
error_solution_tab.pack(expand=True, fill="both", padx=10, pady=5)

# Etiquetas y campos de entrada usando pack()
label_func = tk.Label(root, text="Ecuación diferencial (en términos de x e y):")
label_func.pack(anchor="w", padx=10, pady=5)

entry_func = tk.Entry(root, width=30)
entry_func.pack(padx=10, pady=5)

label_x0 = tk.Label(root, text="x0 (valor inicial de x):")
label_x0.pack(anchor="w", padx=10, pady=5)

entry_x0 = tk.Entry(root, width=10)
entry_x0.pack(padx=10, pady=5)

label_y0 = tk.Label(root, text="y0 (valor inicial de y):")
label_y0.pack(anchor="w", padx=10, pady=5)

entry_y0 = tk.Entry(root, width=10)
entry_y0.pack(padx=10, pady=5)

label_xf = tk.Label(root, text="xf (valor final de x):")
label_xf.pack(anchor="w", padx=10, pady=5)

entry_xf = tk.Entry(root, width=10)
entry_xf.pack(padx=10, pady=5)

label_h = tk.Label(root, text="h (tamaño del paso):")
label_h.pack(anchor="w", padx=10, pady=5)

entry_h = tk.Entry(root, width=10)
entry_h.pack(padx=10, pady=5)

# Botón para resolver la EDO
btn_solve = tk.Button(root, text="Resolver EDO", command=solve_edo)
btn_solve.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
