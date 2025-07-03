## try genérico
#try:
#    number1 = int(input("Numerito: "))
#    number1 = int(input("Numerito: "))
#
#
#try:
#    number1 = int(input("Numerito: "))
#    number1 = int(input("Numerito: "))
#except ValueError:
#    print("Se ha producido un error de tipo ValueError")
#except ZeroDivisionError:
#    print("Se ha producido un error de tipo ")
#
# try except finally (se ejecuta haya o no errores, siempre se ejecuta)
#def miFunción():
#    try:
#        print("sentencia 1")
#    except:
#        print("sentencia 2")
#    finally:
#        print("sentencia 3")
#
#def myFunction():
#    try:
#        print("sentencia 1")
#        x = 10 / 0
#    except:
#        print("sentencia 2")
#    finally:
#        print("sentencia 3")
#
#miFunción()
#myFunction()
#
## try return, en caso de haber un finally se ejecutará antes de parar la ejecución con el return
#def myReturn():
#    try:
#        print("sentencia 1")
#        x = 10 / 0
#        return (1)
#    finally:
#        print("sentencia 2")
#
#print(myReturn())
#print("sentencia 3")
#
#def myReturn():
#    try:
#        print("sentencia 1")
#        x = 10 / 0
#        return (1)
#    except:
#        print("sentencia 2")
#        return (2)
#    finally:
#        print("sentencia 3")
#
#print(myReturn())
#print("sentencia 4")
#def mift():
#    try:
#        print("sentencia 1")
#        x = 10 / 0
#        return 1
#    except:
#        print("sentencia 2")
#        return 2
#    print ("sentencia 3")
#
#print(mift())
## lo que se cambie de una var externa en los try se aplican, el try no trabaja solo dentro del scope
#def mift():
#    x = 13
#    try:
#        print("sentencia 1")
#        x = 1
#        #return 1
#    except:
#        print("sentencia 2")
#        #return 2
#    print (f"X: {x}")
#
#print(mift())
## raise
#num = -1
#if num < 0:
#    raise Exception("Numero no puede ser inferior a 0")
## raise es como una sobrecarga de errores/excepciones
#texto = "sida"
#if not type(texto) in int:
#    raise TypeError("El dato introducido debe ser un entero")
import datetime

currentTime = datetime.datetime.now()

p