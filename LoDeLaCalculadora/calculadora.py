import os
import time
from mylib import suma, resta, producto, division

while (True):
    os.system("clear")
    print("CALCULADORA")
    print("***********\n")
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    os.system("clear")
    print("CALCULADORA")
    print("***********\n")
    print("1) SUMA")
    print("2) RESTA")
    print("3) PRODUCTO")
    print("4) DIVISION")
    print("5) SALIR")

    ex = int(input("Seleción: "))
    os.system("clear")
    if (ex == 1):
        print(f"Resultado: {suma(a, b)}")
        input("\nContinuar...")
    elif (ex == 2):
        print(f"Resultado: {resta(a, b)}")
        input("\nContinuar...")
    elif (ex == 3):
        print(f"Resultado: {producto(a, b)}")
        input("\nContinuar...")
    elif (ex == 4):
        print(f"Resultado: {division(a, b)}")
        input("\nContinuar...")
    elif (ex == 5):
        print("¡Chao, chao, chachaochao!")
        time.sleep(1)
        break
    else:
        print("Opción inválida")
        time.sleep(1)
os.system("clear")
