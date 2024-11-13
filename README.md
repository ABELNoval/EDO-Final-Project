
# EDO Solver - Método de Euler

Este repositorio contiene una aplicación para resolver ecuaciones diferenciales ordinarias (EDO) utilizando el método de Euler. Este enfoque numérico es una solución sencilla y eficaz para aproximar soluciones de EDOs de primer orden.

## Características

- Resolución de ecuaciones diferenciales ordinarias de primer orden.
- Implementación clara y optimizada del método de Euler.
- Visualización gráfica de los resultados para un análisis intuitivo.
- Uso opcional de una interfaz de usuario sencilla (si aplica).

---

## Requisitos Previos

Asegúrate de tener instalado Python (versión 3.6 o superior). Se recomienda utilizar un entorno virtual para gestionar las dependencias y mantener el proyecto aislado de otros entornos.

### Librerías necesarias

- **NumPy**: Para cálculos numéricos eficientes.
- **Matplotlib**: Para la visualización gráfica de resultados.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/edo-solver-euler.git
cd edo-solver-euler
```

### 2. Crear un entorno virtual

Para mantener las dependencias aisladas, crea un entorno virtual:

```bash
python -m venv env
```

Activa el entorno:

- En **Windows**:
  ```bash
  .\env\Scripts\activate
  ```
- En **Linux/macOS**:
  ```bash
  source env/bin/activate
  ```

### 3. Instalar dependencias

Usa el archivo `requirements.txt` para instalar todas las librerías necesarias:

```bash
pip install -r requirements.txt
```

---

## Uso

Para ejecutar la aplicación:

```bash
python main.py
```

### Personalización

Modifica el archivo principal (`main.py`) para definir la EDO, las condiciones iniciales y el intervalo de tiempo que deseas analizar.

---

## Visualización

El programa generará gráficos interactivos que mostrarán la solución aproximada obtenida con el método de Euler. Puedes personalizar los colores y estilos de las gráficas según tus preferencias.

---

## Contribuciones

### Ramas del repositorio

Este proyecto utiliza la siguiente estructura de ramas para mantener el código organizado:

- **main**: Contiene el código listo para producción.
- **develop**: Para el desarrollo activo y pruebas de nuevas características.
- **feature/**: Ramas específicas para implementar nuevas funcionalidades. Ejemplo: `feature/visualization`.

### Cómo contribuir

1. Crea un fork del repositorio.
2. Crea una rama desde `develop`:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commits descriptivos.
4. Envía un pull request a la rama `develop`.

---

## Notas sobre Python

Python es un lenguaje de programación de alto nivel que es ampliamente utilizado en matemáticas y análisis numérico debido a su simplicidad y capacidad de manejar cálculos complejos. Utilizar un entorno virtual asegura que las dependencias no entren en conflicto con otros proyectos.

---

¡Gracias por usar EDO Solver - Método de Euler! Si tienes alguna sugerencia o problema, no dudes en abrir un *issue*.

---

### Ejemplo de `requirements.txt`

```txt
numpy>=1.21.0
matplotlib>=3.4.0
```
