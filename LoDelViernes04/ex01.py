# Enunciado: Crear un programa que permita registrar estudiantes, calcular sus notas medias, determinar si apruebam, y mostrar un resumen completo usando clases, funciones, condicionales, estructuras de decisión y variables.

import os

def limpiarConsola():
    operativeSystem = os.name
    if (operativeSystem == "nt"):
        os.system("cls")
    elif (operativeSystem == "posix"):
        os.system("clear")

def continuar():
    input("Continuar...")

class Estudiante():
    def __init__(this, nombre, apellido, notas):
        this.nombre = nombre
        this.apellido = apellido
        this.notas = notas

    def verDatos(this):
        print(f"Estuadiante: {this.nombre} {this.apellido}")
        i = 1
        for nota in this.notas:
            print(f"    Examen {i}: {nota}")
            i+=1
        print("")

class Registro():
    estudiantes = []

    def añadirEstudiante(this):
        nombre = input("Nombre: ")
        limpiarConsola()
        apellido = input("Apellido: ")
        notas = []
        i = 0
        while (True):
            limpiarConsola()
            print("Introduce un valor no numérico para finalizar el registro")
            i+=1
            nota = input(f"Nota Examen {i}: ")
            if (nota.isalnum() == True):
                notas = notas + [float(nota)]
            else:
                break
        this.estudiantes = this.estudiantes + [Estudiante(nombre, apellido, notas)]

    def verRegistro(this):
        print("--- Registro de Estudiantes ---")
        i = 0
        for value in this.estudiantes:
            i+=1
            print(f"    {i} - {value.nombre} {value.apellido}")

    def verNotasUsuario(this, index):
        user = this.estudiantes[index - 1]
        print(f"--- Notas de {user.nombre} {user.apellido}---")
        i = 0
        for nota in user.notas:
            i+=1
            print(f"Nota Examen {i}: {nota}")

    def verNotasTotal(this):
        i = 0
        for user in this.estudiantes:
            i+=1
            this.verNotasUsuario(i)

    def mediaNotas(this, user):
        total = 0
        for nota in user.notas:
            total+=nota
        return (total / len(user.notas))

    def verAptoUsuario(this, index):
        user = this.estudiantes[index - 1]
        media = this.mediaNotas(user)
        if (media >= 5):
            print(f"Nota media de {user.nombre} {user.apellido}: {round(media, 2)} - Apto")
        else:
            print(f"Nota media de {user.nombre} {user.apellido}: {round(media, 2)} - No apto")

    def verAptoTotal(this):
        i = 0
        for user in this.estudiantes:
            i+=1
            this.verAptoUsuario(i)


def menu():
    limpiarConsola()
    print("--- Bienvenido al registro de notas de los estudiantes ---")
    print("1 - Añadir un nuevo estudiante y notas al registro.")
    print("2 - Ver registro")
    print("3 - Ver notas de un estudiantes por indice")
    print("4 - Ver todas las notas de todos los usuarios")
    print("5 - Ver estudiantes aptos según la media de exámenes realizados")
    print("6 - Salir")
    return (input("Opción: "))

def main():
    limpiarConsola()
    registro = Registro()

    while (True):
        op = menu()
        if (op == "1"):
            limpiarConsola()
            registro.añadirEstudiante()
            continuar()
        elif (op == "2"):
            limpiarConsola()
            registro.verRegistro()
            continuar()
        elif (op == "3"):
            limpiarConsola()
            registro.verNotasUsuario(int(input("Índice de usuario: ")))
            continuar()
        elif (op == "4"):
            limpiarConsola()
            registro.verNotasTotal()
            continuar()
        elif (op == "5"):
            limpiarConsola()
            registro.verAptoTotal()
            continuar()
        elif (op == "6"):
            break
        elif (op == ""):
            pass
        else:
            limpiarConsola()
            print("Opción inválida")
            continuar()
            

main()