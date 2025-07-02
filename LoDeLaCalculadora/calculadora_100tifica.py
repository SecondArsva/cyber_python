import os
import time
import random
from mylib import suma, resta, producto, division, lstadd, lstsum, lstmedia, lstpoles, lstview, lstfactorial, fibonacci

lst = [1, 2, 3]

while (True):
    os.system("clear")
    print("--- Calculadora de Estadísticas y Secuencuas ---")
    print("1. Crear nueva lista numérica")
    print("2. Mostrar suma")
    print("3. Mostrar promedio")
    print("4. Mostrar máximo y mínimo")
    print("5. Calcular factorial")
    print("6. Calcular número de Fibonacci")
    print("7. Mostrar demo funciones lambda")
    print("8. Ver contenido de la lista")
    print("9. Salir")
    ex = int(input("Seleccione una opcion (1-8): "))
    os.system("clear")
    if (ex == 1):
        lst = []
        lst = lstadd()
    elif (ex == 2):
        print(lstsum(lst))
        input("Continuar...")
    elif (ex == 3):
        print(lstmedia(lst))
        input("Continuar...")
    elif (ex == 4):
        print(f"List: {lst}\nMax: {lstpoles(lst)[0]}\nMin: {lstpoles(lst)[1]}")
        input("Continuar...")
    elif (ex == 5):
        lstview(lst)
        print(f"Factoriales: {lstfactorial(lst)}")
        input("Continuar...")
    elif (ex == 6):
        num = random.choice(lst)
        print(f"Sucesión de Fibonacci: {fibonacci(num)}")
        input("Continuar...")
    elif (ex == 7):
        pass # Este no lo tengo aún
    elif (ex == 8):
        lstview(lst)
        input("Contiuar...")
    elif (ex == 9):
        print("¡Chao, chao, chachaochao!")
        time.sleep(1)
        break
    elif (ex == ""):
        pass
    else:
        print("Opción inválida")
        time.sleep(1)
os.system("clear")
