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
    length = lst
    print(length)
    result = 0
    for val in lst:
        result += val
    return (result//length)
