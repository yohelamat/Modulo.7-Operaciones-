import operaciones

def calculadora():
    print("Calculadora")
    try:
        num1 = float(input("Porfavor ingresa el primer valor: "))
        num2 = float(input("Porfavor ingresa el segundo valor: "))
    except ValueError:
        print("Error. Porfavor solo introduce valores numericos.")
        return

    print("\nSelecciona la operación que deseas realizar :")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Introduce la opción deseada (1, 2, 3 o 4): ")
    if opcion == '1':
        resultado = operaciones.sumar(num1, num2)
        operacion_simbolo = "+"
    elif opcion == '2':
        resultado = operaciones.restar(num1, num2)
        operacion_simbolo = "-"
    elif opcion == '3':
        resultado = operaciones.multiplicar(num1, num2)
        operacion_simbolo = "*"
    elif opcion == '4':
        resultado = operaciones.dividir(num1, num2)
        operacion_simbolo = "/"
    else:
        print("\nError. Opcion seleccionada incorrecta.")
        return

    print(f"\nEl resultado de {num1} {operacion_simbolo} {num2} es: {resultado}")

if __name__ == "__main__":
    calculadora()