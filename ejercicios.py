# Tanda de ejercicios correspondientes al PDF - Davidga2
import random
numEx = int(input("Introduce el número del ejercicio a revisar\nTu elección: "))
if (numEx == 100):
    numA = int(input("Edad: "))
    if (numA >= 18):
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
if (numEx == 105):
    numA = int(input("Numerito A: "))
    numB = int(input("Numerito B: "))
    if (numA == numB):
        print("A y B son iguales")
    elif (numA > numB):
        print("A es mayor a B")
    else:
        print("B es mayor a A")
if (numEx == 110):
    numA = int(input("Calificación: "))
    if (numA >= 90):
        print("Exelente")
    elif (numA >= 70 and numA < 90):
        print("Bueno")
    elif (numA < 70 and numA >= 50):
        print("Suficiente")
    else:
        print("Insuficiente")
if (numEx == 115):
    numA = int(input("Gasto total: "))
    if (numA >= 1000):
        discount = (15 * 1000) / 100
        total = 1000 - discount
        print(f"Aplicado el descuento del 15%\nQue en su caso son {discount}\nHa de pagar un total de {total}€")
    else:
        print("Para recibir el descuento ha de gastar mínimo 1000€")
if (numEx == 120):
    numA = int(input("Introduzca un día de la semana de forma numérica: "))
    if (numA > 0 and numA < 8):
        if (numA == 1):
            print("Lunes")
        elif (numA == 2):
            print("Martes")
        elif (numA == 3):
            print("Miércoles")
        elif (numA == 4):
            print("Jueves")
        elif (numA == 5):
            print("Viernes")
        elif (numA == 6):
            print("Sábado")
        else:
            print("Domingo")
    else:
        print("No existen días dentro de ese rango")
if (numEx == 125):
    numA = int(input("Edad: "))
    if (numA < 0):
        print("Nonato")
    elif (numA < 13):
        print("Niño")
    elif(numA < 20):
        print("Adolescente")
    elif(numA < 65):
        print("Adulto")
    else:
        print("Adulto mayor")
if (numEx == 130):
    numA = int(input("Calificación: "))
    if (numA < 0 and numA > 100):
        if (numA < 50):
            print("Insuficiente")
        elif(numA < 60):
            print("Suficiente")
        elif(numA < 70):
            print("Bien")
        elif(numA < 90):
            print("Muy bien")
        else:
            print("Excelente")
    else:
        print("Nota fuera de rango")
elif (numEx == 135):
    numA = int(input("Temperatura en grados celsius: "))
    if (numA < 10):
        print("Recomendación: Abrigo y bufanda")
    elif (numA < 19):
        print("Recomendación: Suéter ligero")
    else:
        print("Recomendación: Camiseta")
elif (numEx == 140):
    numA = int(input("Ingresos anuales: "))
    if (numA < 48000):
        print("Sueldo bajo")
    elif (numA < 96000):
        print("Sueldo medio")
    else:
        print("Sueldo alto")
elif (numEx == 145):
    numA = int(input("Valor de compra: "))
    discount = 0
    if (numA >= 100):
        discount = (10 * numA) / 100
    elif (numA >= 500):
        discount = (20 * numA) / 100
    print(f"Descuento aplicado: {numA - discount}€")
elif (numEx == 150):
    numA = int(input("Edad: "))
    if (numA >= 18):
        numB = int(input("Dinero ahorrado: "))
        if (numB >= 20000):
            print("Vehículo concedido")
        else:
            print("Necesitas mínimo 20.000€")
    else:
        print("Vuelve cuando seas mayor de edad.")
elif (numEx == 155):
    numRand = random.randint(0, 100)
    while (True):
        numA = int(input("Numerito (1 al 100): "))
        if (numA >= 1 and numA <= 100):
            if (numA > numRand):
                print("El número a adivinar es menor al introducido.")
            elif (numA < numRand):
                print("El número a adivinar es mayor al introducido.")
            else:
                print(f"Acertaste, el valor era {numRand}")
                break
        else:
            print("¡Del 1 al 100, cateto!")
else:
    print(f"{numEx}: Ejercicio inválido")
    print("Listado de ejercicios: ")
    print(" 100 105 110")
    print(" 115 120 125")
    print(" 130 135 140")
    print(" 145 150 155")
