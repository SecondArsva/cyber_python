import os
import time
from mylib import suma, resta, producto, division, lstadd, lstsum, lstmedia

while (True):
    os.system("clear")
    print("--- Calculadora de Estadísticas y Secuencuas ---")
    print("1. Agregar números")
    print("2. Mostrar suma")
    print("3. Mostrar promedio")
    print("4. Mostrar máximo y mínimo")
    print("5. Calcular factorial")
    print("6. Calcular número de Fibonacci")
    print("7. Mostrar demo funciones lambda")
    print("8. Salir")
    ex = int(input("Seleccione una opcion (1-8): "))
    os.system("clear")
    if (ex == 1):
        lst = lstadd()
    elif (ex == 2):
        print(lstsum(lst))
        input("Continuar...")
    elif (ex == 3):
        print(lstmedia(lst))
    elif (ex == 7):
        pass
    elif (ex == 8):
        print("¡Chao, chao, chachaochao!")
        time.sleep(1)
        break
    else:
        print("Opción inválida")
        time.sleep(1)
os.system("clear")
