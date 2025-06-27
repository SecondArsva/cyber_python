import os

os.system("clear")
print("Ejercicios de listas. Rango del 1 al 6\n")
print("1 - El mensaje secreto")
print("2 - Intercambio de posiciones")
print("3 - El sándwich de listas")
print("4 - Duplicando la lista")
print("5 - Extrayendo el centro")
print("6 - Reversa parcial")
ex = int(input("\nTu elección: "))
os.system("clear")
if (ex == 1):
    myStr = "Código secreto"
    myList = []
    newList = []

    for char in myStr:
        myList = myList + [char]
    print(myList)

    myListStr = ''.join(myList)
    pos = myListStr.find("secreto")
    
    newListStr = myListStr[pos : pos+len("secreto")]
    for char in newListStr:
        newList = newList + [char]
    print(newList)
elif (ex == 2):
    myList = [10, 20, 30, 40, 50]
    print(f"Lista original: {myList}")
    myCopy = myList
    myList[0] = myCopy[len(myList) - 1]
    myList[len(myList) - 1] = myCopy[0]
    print(f"Intercambio aplicado: {myList}")
elif (ex == 3):
    top = ["rebanada superior"]
    ingredientes = ["jamón", "queso", "tomate"]
    bot = ["rebanada inferior"]
    sandwich = top + ingredientes + bot
    print(sandwich)
elif (ex == 4):
    myList = [1, 2, 3]
    newList = myList + myList
    print(myList)
    print(newList)
elif (ex == 5):
    myList = [1, 2, 3, 4, 5]
    center = (len(myList) - 1) / 2
    print(myList)
    print(f"El valor central es: {myList[int(center)]}")
elif (ex == 6):
    # <myway>
    # myCopy = myList no crea una nueva lista, sino una referencia
    myList = [1,2,3,4,5,6]
    myCopy = []
    for i in myList:
        myCopy = myCopy + [i]
    center = (len(myList) - 1) / 2
    j = int(center + 1) - 1
    # print(f"j = {j}")
    # print(f"My List: {myList}")
    # print(f"My Copy: {myCopy}")
    # print(f"Centro: {center}")
    # print(f"Centro int: {j}")
    for i in range(0, j + 1):
        #print(f"i: {i}  j: {j - i}")
        myList[i] = myCopy[(j - i)]
    print(myList)
    # </myway>
    # <pythonishway>
    lista = [1,2,3,4,5,6,7,8]
    mitad = len(lista) // 2

    primera_mitad_invertida = list(reversed(lista[:mitad]))
    nueva_lista = primera_mitad_invertida + lista[mitad:]

    print(nueva_lista)

    # </pythonishway>
else:
    print("Opción inválida")


# imprimir una lista en la que aparezcan los cuadrados del 0 al 9 sin lista de compresión
# y luego con una lista de compresión