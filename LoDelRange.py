import os

os.system("clear")
ex = int(input("El listado de ejercicios va del 1 al 6\nSelección: "))
os.system("clear")
if (ex == 1):    
    print("Impresión de números con for y range")
    for num in range(1, 11):
        print(f"{num}")
elif (ex == 2):
    print("Impresión de impares del 1 al 20 usando for y range")
    for num in range (1, 21):
        if (num % 2 != 0):
            print(num)
elif (ex == 3):
    numA = int(input("Numerito para imprimir su múltiplos: "))
    for num in range(1, (numA * 10) + 1):
        if (num % numA == 0):
            print(num)
elif (ex == 4):
    print("Impresión de números en orden inverso")
    for num in range(10, 0, -1):
        print(num)
elif (ex == 5):
    print("Suma de todos los números dentro de un rango.")
    bot = int(input("Numerito de apertura: "))
    top = int(input("Numerito de cierre: "))
    total = 0
    for num in range(bot, top + 1):
        total+=num
    os.system("clear")
    print(f"Rango: {bot} al {top}")
    print(f"Resultado: {total}")
elif (ex == 6):
    numA = int(input("Tabla del: "))
    for num in range(1, 11):
        print(f"{numA} x {num} = {num * numA}")
else:
    print("Opción inválida")