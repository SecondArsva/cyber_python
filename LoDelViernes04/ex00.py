# Enunciado: Crear un programa que permita al usuario crear una cuenta
# bancaria, depositar dinero, retirar dinero, consultar el saldo y
# salir del programa. Se deben usar una clase para representar la
# cuenta, funciones para manejar las acciones y estructuras de control
# para gestionar el flujo del programa.

class BankAccount():
    __user = "Unknown"
    __amount = 0

    def __init__(this, userName, moneyAmount):
        this.__user = userName
        this.__amount = moneyAmount
    
    def getUser(this):
        return(this.__user)

    def getAmount(this):
        return (this.__amount)
    
    def depAmount(this, a):
        this.__amount += a
    
    def retAmount(this, a):
        check = this.__amount - a
        if (check >= 0):
            this.__amount -= a
        else:
            print(f"Transacción bloqueada: {this.__user} dejarías tu cuenta a {check}")

    def checkAmount(this):
        print(f"La cuenta de {this.__user}, tiene un saldo de {this.__amount} rupias del Zelda.\nConcretamente del Ocarina of Time.")

def main():
    print("Creación de cuenta bancaria")
    account = BankAccount(str(input("Nombre de usuario: ")), int(input("Saldo: ")))
    
    while (True):
        print("Opciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar Saldo")
        print("4. Salir")
        op = int(input("Opción: "))
        if (op == 1):
            account.depAmount(int(input("Cantidad a depositar: ")))
        elif (op == 2):
            account.retAmount(int(input("Cantidad a retirar: ")))
        elif (op == 3):
            account.checkAmount()
        elif (op == 4):
            exit()
        else:
            print("Opción inválida")

main()