# Python Día 00 - 23/06/2025

import math

#print("¡Hola, Python!") # Esto es un comentario.
#print("Introduce un valor: ")
#foo = input()
#print("Tu valor: " + foo + "\n")
#
#print("--- Variables ---")
#print("String")
#myString = "El miedo mata la mente"
#print("My string: " + myString)
#print(type(myString))
#print("")
#
#print("Int")
#myInt = 288
#print("My int: " + str(myInt))
#print(type(myInt))
#print("")
#
#print("Float")
#myFloat = 3.14
#print("My float: " + str(myFloat))
#print(type(myFloat))
#print("")
#
#print("Bools")
#myBool = True
#print("My bool: " + str(myBool))
#print(type(myBool))
#
#print("")
#print("--- Conversiones ---")
## convierte una cadena a un entero y súmalo a otro entero:
#myString = "98"
#print(int(myString) + 1)
#
#
## convierte un entero a cadena y concatena la cadena a un entero:
#myInt = 99
#print(str(myInt) + str(1))
#
#print("")
#print("--- Tuplas/Listas ---")
## Las tuplas son arrays como los de C. Fijos, no alterables.
#
## las listas permiten reasignar o eliminar contenidos.
#lista = ["Sida", "Noda"]
#print("Len lista" + str(len(lista)))
#print(lista[0])
#print(lista[1])
## adición
#lista += ["Nodo"]
#print("Len lista" + str(len(lista)))
#print(lista[2])
## borrado
#del(lista[2])
#print("Len lista" + str(len(lista)))
#
#print("")
#print("--- Métodos ---")
#myString = "El miedo mata la mente."
#print("Capitalize: " , myString.capitalize())
#print("Lower: " , myString.lower())
#print("Upper: " , myString.upper())
#print("Find: " , myString.find("mata"))
#print("Isalnum: " , myString.isalnum())
#print("Isalpha: " , myString.isalpha())
#print("Isnumeric: " , myString.isnumeric())
#
#currDate = "23/06/2025"
#print(currDate.split("/"))
#myString = "$%&&%$El miedo mata la mente$%$%"
#print(myString.strip("%$&"))
#
#print("--- Operadores Lógicos ---")
#a = True
#b = False
#print(a and b)
#print(a or b)
#print(not b)
#
## suma dos dos numeros ingresados por teclado, que sean float
## y el resultado salga en el print:
#print("Introduce dos floats: ")
#numA = float(input())
#numB = float(input())
#print("Resultado: ", numA + numB)
#
## importar librería
#import math
#piVar = math.pi
#print("Pi value: ", piVar)
#
#numA = 2
#numB = 3
#print(str(numA) + " elevado a " + str(numB) + ": " + str(numA ** numB))
#print(f"Formateado ")
#
## impresión de tipos
#myStr = str(input("Introduce un str: "))
#myInt = int(input("Introduce un int: "))
#myFloat = float(input("Introduce un float: "))
#print(f"String:  {type(myStr)}")
#print(f"Integer:  {type(myInt)}")
#print(f"Float:  {type(myFloat)}")
#
## sacar el último número de un entero recibido
#myInt = input("Numerito: ")
#print(myInt%10)
#
## divisiones (el "//" muestra el resultado sin decimales)
#print("10 / 3: " + str(10/3))
#print("10 // 3: " * str(10//3))
#
## valor a y b por teclado, enteros, cociente entre a y b, b y a.
#numA = input("Numerito A:")
#numB = input("Numerito b:")
#
## valor por teclado. calcular IVA (21%) y aplicarlo
# numA = float(input("Numerito: "))
# iva = 21
# reglaDeTres = (numA * iva) / 100
# resultado = numA + reglaDeTres
# print(f"Valor introducido: {numA}")
# print(f"IVA a aplicar: {reglaDeTres}")
# print(f"Iva aplicado: {round(resultado, 2)}€")
# 
# # pillar un texto que se repita N veces
# myStr = input("Introduce un string: ")
# numA = int(input("Introduce un número de veces a repetir el texto: "))
# print(myStr * numA)
## ¿Calcular el área de un rectángulo?
#print("Calcular el área de un rectángulo")
#numA = int(input("Primer par de lados: "))
#numB = int(input("Segundo par de lados: "))
#print("Área de tu rectángulo: ", (numA * 2) + (numB * 2))
#
## convertir minutos a dia, hora y munutos
#numA = int(input("Numerito: "))
#min = 
## Perdir por cosola una edad y cosiderar como error los valores
## introducidos a partir de 100
#myInt = int(input("Introduzca su edad: "))
#if (myInt > 99):
#    print(f"Error: con {myInt} años debería estar muerto")
#elif (myInt < 18):
#    print(f"Con {myInt} años madura un poco")
#else:
#    print("¡Acceso concedido!")
## Pillar numA y numB, usan ternarios imprime si A es mayor a B
## Supuestamente ese if es un ternario.
#numA = int(input("Numerito A: "))
#numB = int(input("Numerito B: "))
#if (numA > numB): print(numA, " es mayor a ", numB)
#
##
#myInt = int(input("Numerito: "))
#if (0<myInt<100):
#    print(f"Tu número se encuentra entre 0 y 100")
#else:
#    print(f"Tu número está fuera de rango")
## Pedimos 4 enteros equivalentes a 4 salarios: presidente, director, jefe y operario.
## Si el salario del operario es menor a todos los demás, ok. Sino, error.
## Si el salario del que le precede es mayor, mal.
#numA = int(input("Salario Presidente: "))
#numB = int(input("Salario Director: "))
#numC = int(input("Salario Jefe: "))
#numD = int(input("Salario Operario: "))
#if (numA>numB>numC>numD):
#    print("\n¡Salarios en orden!")
#
## Tres valores: distancia, num hermanos, nota media
## si la distancia es más de 20km o hermanos en menor a 2
## o la nota es menor o igual 5, no se es candidato
## Tiene que cumplir dos condiciones para recibirla
#print("- Datos para la beca -")
#numA = int(input("Distancia a la escuela (en KM): "))
#numB = int(input("Número de hermanos: "))
#numC = int(input("Nota media: "))
#condiciones = 0
#
#if (numA < 20):
#    condiciones+=1
#if (numB >= 2):
#    condiciones+=1
#if (numC > 5):
#    condiciones+=1
#if (condiciones >= 2):
#    print("Beca concedida")
#else:
#    print("Beca denegada")
## Pedir dos valores para pillar un coche. Mas de 18 pasa a la pasta.
## Si tiene 20.000 se le vende, sino, no.
#numA = int(input("Edad: "))
#
#if (numA >= 18):
#    numB = int(input("Dinero ahorrado: "))
#    if (numB >= 20000):
#        print("Vehículo concedido")
#    else:
#        print("Necesitas mínimo 20.000€")
#else:
#    print("Vuelve cuando seas mayor de edad.")

## Tanda de ejercicios correspondientes al PDF
#import random
#numEx = int(input("Introduce el número del ejercicio a revisar\nTu elección: "))
#if (numEx == 100):
#    numA = int(input("Edad: "))
#    if (numA >= 18):
#        print("Eres mayor de edad.")
#    else:
#        print("Eres menor de edad.")
#if (numEx == 105):
#    numA = int(input("Numerito A: "))
#    numB = int(input("Numerito B: "))
#    if (numA == numB):
#        print("A y B son iguales")
#    elif (numA > numB):
#        print("A es mayor a B")
#    else:
#        print("B es mayor a A")
#if (numEx == 110):
#    numA = int(input("Calificación: "))
#    if (numA >= 90):
#        print("Exelente")
#    elif (numA >= 70 and numA < 90):
#        print("Bueno")
#    elif (numA < 70 and numA >= 50):
#        print("Suficiente")
#    else:
#        print("Insuficiente")
#if (numEx == 115):
#    numA = int(input("Gasto total: "))
#    if (numA >= 1000):
#        discount = (15 * 1000) / 100
#        total = 1000 - discount
#        print(f"Aplicado el descuento del 15%\nQue en su caso son {discount}\nHa de pagar un total de {total}€")
#    else:
#        print("Para recibir el descuento ha de gastar mínimo 1000€")
#if (numEx == 120):
#    numA = int(input("Introduzca un día de la semana de forma numérica: "))
#    if (numA > 0 and numA < 8):
#        if (numA == 1):
#            print("Lunes")
#        elif (numA == 2):
#            print("Martes")
#        elif (numA == 3):
#            print("Miércoles")
#        elif (numA == 4):
#            print("Jueves")
#        elif (numA == 5):
#            print("Viernes")
#        elif (numA == 6):
#            print("Sábado")
#        else:
#            print("Domingo")
#    else:
#        print("No existen días dentro de ese rango")
#if (numEx == 125):
#    numA = int(input("Edad: "))
#    if (numA < 0):
#        print("Nonato")
#    elif (numA < 13):
#        print("Niño")
#    elif(numA < 20):
#        print("Adolescente")
#    elif(numA < 65):
#        print("Adulto")
#    else:
#        print("Adulto mayor")
#if (numEx == 130):
#    numA = int(input("Calificación: "))
#    if (numA < 0 and numA > 100):
#        if (numA < 50):
#            print("Insuficiente")
#        elif(numA < 60):
#            print("Suficiente")
#        elif(numA < 70):
#            print("Bien")
#        elif(numA < 90):
#            print("Muy bien")
#        else:
#            print("Excelente")
#    else:
#        print("Nota fuera de rango")
#elif (numEx == 135):
#    numA = int(input("Temperatura en grados celsius: "))
#    if (numA < 10):
#        print("Recomendación: Abrigo y bufanda")
#    elif (numA < 19):
#        print("Recomendación: Suéter ligero")
#    else:
#        print("Recomendación: Camiseta")
#elif (numEx == 140):
#    numA = int(input("Ingresos anuales: "))
#    if (numA < 48000):
#        print("Sueldo bajo")
#    elif (numA < 96000):
#        print("Sueldo medio")
#    else:
#        print("Sueldo alto")
#elif (numEx == 145):
#    numA = int(input("Valor de compra: "))
#    discount = 0
#    if (numA >= 100):
#        discount = (10 * numA) / 100
#    elif (numA >= 500):
#        discount = (20 * numA) / 100
#    print(f"Descuento aplicado: {numA - discount}€")
#elif (numEx == 150):
#    numA = int(input("Edad: "))
#    if (numA >= 18):
#        numB = int(input("Dinero ahorrado: "))
#        if (numB >= 20000):
#            print("Vehículo concedido")
#        else:
#            print("Necesitas mínimo 20.000€")
#    else:
#        print("Vuelve cuando seas mayor de edad.")
#elif (numEx == 155):
#    numRand = random.randint(0, 100)
#    while (True):
#        numA = int(input("Numerito (1 al 100): "))
#        if (numA >= 1 and numA <= 100):
#            if (numA > numRand):
#                print("El número a adivinar es menor al introducido.")
#            elif (numA < numRand):
#                print("El número a adivinar es mayor al introducido.")
#            else:
#                print(f"Acertaste, el valor era {numRand}")
#                break
#        else:
#            print("¡Del 1 al 100, cateto!")
#else:
#    print(f"{numEx}: Ejercicio inválido")
#    print("Listado de ejercicios: ")
#    print(" 100 105 110")
#    print(" 115 120 125")
#    print(" 130 135 140")
#    print(" 145 150 155")
#
## For each
#
#for i in [1, 10]:
#    print("Hola")
#
#for i in ["primavera", "verano", "otoño", "invierno"]:
#    print(i)
#
#for i in "Frase":
#    print("Hola", end=" ")
#
## EMAIL
#myString = input("Introduce un email: ")
#valid = False
#
#for char in myString:
#    if (char == "@"):
#        valid = True
#        break
#
#if (valid == True):
#    print("Email recibido")
#else:
#    print("Email inválido")
#
## RANGE
#for i in range(5):
#    print(f"Valor A: {i}")
#
#for i in range(5, 10):
#    print(f"Valor B: {i}")
#    
#for i in range(5, 10, 2):
#    print(f"Valor C: {i}")
#
#for i in "Banana":
#    print(i)
#
#frutas = ["Manzana", "Fresa", "Banana", "Pera"]
#for i in frutas:
#    if (x == "Banana"):
#        print(x)
## Lista de animales, uno es "Loro". Imprimimos nombre del animal y cuando salga el Loro
## hacemos un break y mostramos su posición
#listAnimal = ["Rata", "Cuervo", "Loro", "Perro"]
#listUpper = [animal.upper() for animal in listAnimal] #Horrible
#print(listUpper)
#
## Recorrer lista numérica y crear otra nueva en base a la primera,
## pero guardando los pares.
#numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#oddList = [num for num in numList if num % 2 == 0] # Obtuso de cojones
#evenList = [num for num in numList if num % 2 != 0]
#print(f"Par: {oddList}")
#print(f"Impar: {evenList}")
## TANDA EJERCICIOS FOR
## Calcula la media de los números de una lista usando un bucle for
#
## Busca el máximo de una lista
## Dada la siguiente lista de números:
## numeros = [15, 5, 25, 10, 20]
## Encuentra el número máximo en la lista usando un bucle for.
#
## Dada la siguiente lista de palabras
## palabras = ["casa", "árbol", "sol", "elefante", "luna"]
## Crea una nueva lista que contenga solo las palabras con máss de 5 letras
## Usando un bucle for y list comprehesion
##
## WHILES
#i = 0
#while (i < 10):
#    print(f"Iteración: {i}")
#    i+=1
#
## Calcula la raíz cuadrada de un número.
## Tenemos tres intentos y el número no puede ser negativo.
#tries = 0
#numA = int(input("Numero a adivinar la raíz cuadrada: "))
#raiz = math.sqrt(numA)
#print("Tienes tres intentos")
#while (tries < 3):
#    numB = int(input("Tu elección: "))
#    if (raiz == numB):
#        print("Número correcto")
#        break
#    elif (tries == 2):
#        print("Fallaste 3 veces. Programa terminado")
#    else:
#        print("Error")
#    tries+=1
#
## While con if anidado y un break
## que salga del bucle cuando una var sea n
#var = 0
#n = 5
#while (True):
#    print(f"Iteración: {var}")
#    if (var == n):
#        print(f"Var es igual a {n}")
#        print(f"Fin del bucle")
#        break
#    var+=1
## Match-Case
#def ft_operacion(opcion):
#    match opcion:
#        case 1:
#            return ("Opción 1 seleccionada")
#        case 2:
#            return ("Opción 2 seleccionada")
#        case 3:
#            return ("Opción 3 seleccionada")
#        case _:
#            return ("Opción fuera de rango (1-3)")
#
#print(ft_operacion(2))
#print(ft_operacion(4))
    