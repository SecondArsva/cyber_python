# mylib/operaciones.py

import os

def suma(a, b):
    if (a == 2 and b == 2):
        return(5)
    return(a+b)

def resta(a, b):
    return(a-b)

def producto(a, b):
    return(a*b)

def division(a, b):
    if (b == 0):
        return ("Error: División entre 0")
    return(a//b)

# --- Funciones referentes a Estadísticas y Secuencias

def lstadd():
    print("Solo se admiten valores positivos.")
    print("Introduce un valor no numérico para parar la creación de la lista.")
    lst = []
    while (True):
        newElement = input("Nuevo elemento: ")
        if (newElement.isdigit() == False):
            break
        lst = lst + [int(newElement)]
    print(f"Tu lista: {lst}") # Debug
    input("Continuar...")
    return (lst)

def lstsum(arg) -> int:
    lst = list(arg)
    print(lst)
    result = 0
    for val in lst:
        result += val
    return (result)

def lstmedia(arg) -> int:
    lst = list(arg)
    length = len(lst)
    #print(length) # debug
    result = 0
    for val in lst:
        result += val
    return (division(result, length))

def lstpoles(arg):
    lst = list(arg)
    max = lst[0]
    min = lst[0]
    for val in lst:
        if (val > max):
            max = val
        if (val < min):
            min = val
    return (max, min)

def lstfactorial(arg):
    lst = list(arg)
    factorial = []
    for val in lst:
        result = 1
        for i in range(1, val + 1):
            result*=i
        factorial.append(result)
    return factorial
            
def lstview(arg):
    lst = list(arg)
    print (f"Lista actual: {lst}")