# Proyecto Calculadora

Este proyecto consiste en una calculadora básica implementada en Python, que incluye una interfaz de línea de comandos y un conjunto de pruebas unitarias para verificar su funcionamiento.

## Descripción de los archivos

### `calculadora.py`
Este es el archivo principal de la aplicación. Contiene:
- **Funciones Aritméticas**: Definiciones para `sumar`, `restar`, `multiplicar` y `dividir`.
- **Interfaz de Usuario (CLI)**: La función `calculadora()` implementa un bucle interactivo que permite al usuario seleccionar una operación e introducir los números deseados.
- **Manejo de Errores**: Gestiona entradas no válidas y evita la división por cero lanzando y capturando excepciones.
- **Punto de Entrada**: El bloque `if __name__ == "__main__":` permite ejecutar el script directamente.

### `test.py`
Este archivo se encarga del aseguramiento de la calidad del código (QA).
- **Framework `unittest`**: Utiliza la biblioteca estándar de Python para realizar pruebas automatizadas.
- **Clase `TestOperaciones`**: Define casos de prueba para cada operación matemática, verificando que los resultados sean correctos tanto para enteros como para flotantes y números negativos.
- **Pruebas de Excepciones**: Verifica específicamente que la función de división lance un `ValueError` cuando se intenta dividir por cero.