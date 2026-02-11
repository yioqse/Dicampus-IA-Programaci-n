## Proyecto Calculadora

### `Calculadora/calculadora.py`
Este script implementa una calculadora básica interactiva por línea de comandos.
- **Funciones Aritméticas**: Define funciones puras para `sumar`, `restar`, `multiplicar` y `dividir`.
- **Manejo de Errores**: La función de división lanza un `ValueError` si se intenta dividir por cero.
- **Interfaz de Usuario**: La función `calculadora()` ejecuta un bucle infinito que muestra un menú, captura la entrada del usuario y muestra los resultados, manejando excepciones de entrada (como texto en lugar de números).

### `Calculadora/test.py`
Este archivo contiene el conjunto de pruebas unitarias para validar la lógica de la calculadora.
- **Framework**: Utiliza el módulo estándar `unittest`.
- **Cobertura**:
  - Verifica resultados correctos para enteros y números de punto flotante (`assertAlmostEqual`).
  - Comprueba el manejo de números negativos.
  - Valida que la división por cero lance la excepción correcta (`assertRaises`).