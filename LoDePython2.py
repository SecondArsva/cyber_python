import os # system
import random # rendint
import time # sleep

os.system("clear")
print('Listado de ejercicios de "LoDelPython2"\n')
print("1 - Números primos en una lista")
print("2 - Contador de vocales y consonantes")
print("3 - Tabla de cajero automático")
print("4 - Tabla de multiplicar con detección par/impar")
print("5 - Validador de contraseñas")
print("6 - Tirada de dado hasta obtener un número generado")
print("7 - Clasificación de números")
print("8 - Juego de adivinanza con número secreto")
print("9 - Cálculo de factorial")
print("10 - Primer número mayor a 100 divisible por un número generado")
ex = int(input("\nTu elección: "))
os.system("clear")
if (ex == 1):
	print("Introduce valores numéricos de uno en uno para añadirlos a una lista.")
	print('Si introduces el "0" se finalizacrá la creación de la misma.')
	print('Posteriormente se revisarán los contenidos de la lista para determinar,\n' \
	'cuales son primos y cuales no.\n')
	numList = []

	while (True):
		numA = int(input("Nuevo valor: "))
		if (numA == 0):
			os.system("clear")
			break
		else:
			numList = numList + [numA]

	def is_prime(num):
		if (num < 2):
			return (False)
		i = 2
		while (i < num):
			if (num % i == 0):
				return (False)
			i+=1
		return (True)
	
	for num in numList:
		if (is_prime(num)):
			print(f'- "{num}" es primo')
		else:
			print(f'- "{num}" no es primo')
elif (ex == 2):
	myStr = input("Ingresa una cadena de texto: ")
	vocales = 0
	consonantes = 0
	otros = 0

	for char in myStr.lower():
		if (char in ['a', "e", 'i', "o", 'u']):
			vocales+=1
		elif (char in 'bcdfghjklmnñpqrstvwxyz'):
			consonantes+=1
		else:
			otros+=1

	def ft_vo(total):
		if (total == 1):
			return ("vocal")
		else:
			return ("vocales")
		
	def ft_co(total):
		if (total == 1): return ("consonante")
		else: return ("consonantes")

	def ft_ex(total):
		if (total == 1):
			return(f"\nAdemás de otro {otros} carácter fuera del marco de los primeros dos tipos.")
		elif (total > 1):
			return(f"\nAdemás de otros {otros} carácteres fuera del marco de los primeros dos tipos.")
		else:
			return("")
		
	print(f'\nTu cadena "{myStr}" contiene: un total de {vocales} {ft_vo(vocales)} y {consonantes} {ft_co(consonantes)}.{ft_ex(otros)}')
elif (ex == 3):
	saldo = random.randint(0, 20000)
	while (True):
		os.system("clear")
		print("¡Bienvenido a este nuestro ficticio sistema bancario!")
		print("Elija una operación de entre las siguientes:")
		print("\n1 - Comprobar saldo\n2 - Ingresar saldo\n3 - Retirar saldo\n4 - Cerrar sesión")
		myStr = input("\nOperación: ")
		if (myStr == "1"):
			os.system("clear")
			print(f"Su saldo actual es de {saldo}€")
			input("\nContinuar...")
		elif (myStr == "2"):
			os.system("clear")
			saldo+=int(input("A ingresar: "))
		elif (myStr == "3"):
			os.system("clear")
			aRetirar = int(input("A retirar: "))
			if ((saldo - aRetirar) < 0):
				os.system("clear")
				print("Operación cancelada: Petición de un valor mayor al saldo disponible")
				input("\nContinuar...")
			else:
				saldo-=aRetirar
		elif (myStr == "4"):
			os.system("clear")
			break
		else:
			os.system("clear")
			print("¡Operación inválida!")
			input("\nContinuar...")
elif (ex == 4):
	numA = int(input("Numerito: "))

	def ft_tipo(result):
		if (result % 2 == 0):
			return(f"es par")
		else:
			return(f"es impar")
	
	print("")
	for i in range(1, 11):
		print(f"{numA} x {i} = {numA * i}	| {ft_tipo(numA * i)}")
elif (ex == 5):
	print("Ingrese una contraseña que contenga un mínimo de 8 carácteres, una mayúscula y un número")
	myStr = input("Contraseña: ")
	characters = 0
	capital = 0
	numbers = 0
	
	for char in myStr:
		characters+=1
		if (char in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
			capital+=1
		if (char in "0123456789"):
			numbers+=1
	if (characters >= 8 and capital >= 1 and numbers >= 1):
		print("Contraseña aceptada.")
	else:
		print("Contraseña inválida: ")
		if (characters < 8):
			print("- No contiene un mínimo de 8 carácteres.")
		if (capital < 1):
			print("- No contiene ni una mayúscula.")
		if (numbers < 1):
			print("- No contiene ni un número.")
elif (ex == 6):
	numA = random.randint(1, 6)
	tries = 0

	print("Programa de tiradas automáticas de un D6 hasta conseguir el número generado.\n")
	print(f"Número generado: {numA}\n")
	while (True):
		dice = random.randint(1, 6)
		tries+=1
		print(f"Tirada número {tries} con resultado {dice}")
		if (numA == dice):
			break
elif (ex == 7):
	print("Introduce 5 enteros de uno en uno para construir y analizar una lista.\n")
	numList = []
	min = 0
	pos = 0
	zero = 0

	for i in range(1, 6):
		numList = numList + [int(input(f"Valor {i}: "))]
	for i in numList:
		if (i > 0):
			pos+=1
		elif (i < 0):
			min+=1
		else:
			zero+=1
	print(f"\nPositivos: {pos}\nNegativos: {min}\nCerapios: {zero}")
elif (ex == 8):
	num = random.randint(1, 50)

	print("Adivina el numerito secreto")
	while (True):
		numA = int(input("Tu numerito: "))
		if (num < numA):
			print("Apunta hacia abajo")
		elif (num > numA):
			print("Apunta hacia arriba")
		else:
			break
	print(f"¡Enhorabuena!\nEl numero secreto era {num}")
elif (ex == 9):
	num = int(input("Numerito: "))

	if num < 0:
		print("El número debe ser positivo.")
	else:
		factorial = 1
		for i in range(1, num + 1):
			factorial *= i
	print(f"El factorial de {num} es {factorial}")
elif (ex == 10):
	num = int(input("Numerito para buscar un valor superior a 100 que sea divisible entre él: "))
	i = 100

	while (i % num != 0):
		i+=1
	print(f"El primer número divisible entre {num} a partir del 100 es el {i}")
else:
	print(f"{ex}: ejercicio inválido")