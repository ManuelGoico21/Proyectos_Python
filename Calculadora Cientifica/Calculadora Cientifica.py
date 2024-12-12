# Programa de calculadora científica

import math

def calculadora_cientifica():
    print("Calculadora Científica")
    print("------------------------")

    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Logaritmo natural")
        print("8. Seno")
        print("9. Coseno")
        print("10. Tangente")
        print("11. Salir")

        opcion = input("Ingrese la opción: ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado: ", num1 + num2)
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado: ", num1 - num2)
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado: ", num1 * num2)
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 != 0:
                print("Resultado: ", num1 / num2)
            else:
                print("Error: No se puede dividir por cero")
        elif opcion == "5":
            num1 = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            print("Resultado: ", num1 ** exponente)
        elif opcion == "6":
            num = float(input("Ingrese el número: "))
            print("Resultado: ", math.sqrt(num))
        elif opcion == "7":
            num = float(input("Ingrese el número: "))
            print("Resultado: ", math.log(num))
        elif opcion == "8":
            num = float(input("Ingrese el ángulo en grados: "))
            print("Resultado: ", math.sin(math.radians(num)))
        elif opcion == "9":
            num = float(input("Ingrese el ángulo en grados: "))
            print("Resultado: ", math.cos(math.radians(num)))
        elif opcion == "10":
            num = float(input("Ingrese el ángulo en grados: "))
            print("Resultado: ", math.tan(math.radians(num)))
        elif opcion == "11":
            print("Adiós")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

calculadora_cientifica()

