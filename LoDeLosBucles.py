import os
os.system("clear")
print("Selecciona un ejercicio")
print(" 210 215 220")
print(" 225 235 240")
print(" 245 250")
ex = int(input("Elección: "))
os.system("clear")
if (ex == 210):
    for i in range(1, 101):
        print(i)
elif (ex == 215):
    for i in range(1, 11):
        print(i ** 2)
elif (ex == 220):
    myStr = input("Introduce una cadena de texto: ")
    myChar = input("Introduce una letra a encontrar en la cadena: ")
    counter = 0
    for i in myStr:
        if (i == myChar):
            counter+=1
    print(f'El carácter "{myChar}" aparece {counter} veces.')
elif (ex == 225):
    numA = int(input("Introduce un número para generar su tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{numA} x {i} = {numA * i}")
elif (ex == 235):
    numA = int(input("Vamos a contar hasta el numerito: "))
    for i in range(1, numA + 1):
        print(i)
elif (ex == 240):
    print("Suma de múltiples valores")
    print('La suma de los valores introducidos,\nse realizará al recibir "0"\n')
    numList = [0]
    while (True):
        numA = int(input("Introduce un valor: "))
        if (numA):
            numList = numList + [numA]
        else:
            break
    print(f"Total: {sum(numList)}")
elif (ex == 245):
    while (True):
        numA = int(input("Introduce un valor: "))
        if (numA == 5):
            print("Por el culo te la hinco.")
            break
elif (ex == 250):
    while (True):
        numA = int(input("Introduce una edad: "))
        if (numA <= 0 or numA >= 101):
            print("Valor incorrecto.")
        else:
            print(f"Edad seleccionada: {numA}")
            break
else:
    print("Opción inválida")