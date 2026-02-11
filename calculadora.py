def sumar(x, y):
    """Esta función suma dos números"""
    return x + y

def restar(x, y):
    """Esta función resta dos números"""
    return x - y

def multiplicar(x, y):
    """Esta función multiplica dos números"""
    return x * y

def dividir(x, y):
    """Esta función divide dos números"""
    if y == 0:
        raise ValueError("No se puede dividir por cero.")
    return x / y

def calculadora():
    """Función principal para ejecutar la calculadora"""
    print("=====================================")
    print("    Calculadora Básica en Python     ")
    print("=====================================")
    
    while True:
        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        # Pedir la elección al usuario
        eleccion = input("Introduce tu elección (1/2/3/4/5): ")

        # Opción para salir del programa
        if eleccion == '5':
            print("\n¡Gracias por usar la calculadora. ¡Hasta luego!")
            break

        # Realizar la operación si la elección es válida
        if eleccion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("\nError: Entrada inválida. Por favor, introduce solo números.")
                continue

            if eleccion == '1':
                print(f"\nResultado: {num1} + {num2} = {sumar(num1, num2)}")

            elif eleccion == '2':
                print(f"\nResultado: {num1} - {num2} = {restar(num1, num2)}")

            elif eleccion == '3':
                print(f"\nResultado: {num1} * {num2} = {multiplicar(num1, num2)}")

            elif eleccion == '4':
                try:
                    resultado = dividir(num1, num2)
                    print(f"\nResultado: {num1} / {num2} = {resultado}")
                except ValueError as e:
                    print(f"\nError: {e}")
        
        else:
            print("\nError: Entrada inválida. Por favor, elige una opción del 1 al 5.")

# Iniciar la calculadora
if __name__ == "__main__":
    calculadora()
