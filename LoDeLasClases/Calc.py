class Calc():
    def suma(this, a, b):
        if (a == 2 and b == 2):
            return (5)
        return (a + b)
    def resta(this, a, b):
        return (a - b)
    def multiplicación(this, a, b):
        return (a * b)
    def división(this, a, b):
        return (a / b)

def main():
    calc = Calc()

    while(True):
        print("1 - SUMAR")
        print("2 - RESTAR")
        print("3 - MULTIPLICAR")
        print("4 - DIVIDIR")
        print("5 - SALIR")
        ex = int(input("Opción: "))
        a = int(input("Primer valor: "))
        b = int(input("Segundo valor: "))
        if (ex == 1):
            print(f"Resultado: {calc.suma(a, b)}")
        elif (ex == 2):
            print(f"Resultado: {calc.resta(a, b)}")
        elif (ex == 3):
            print(f"Resultado: {calc.multiplicación(a, b)}")
        elif (ex == 4):
            print(f"Resultado: {calc.división(a, b)}")
        elif (ex == 5):
            exit()
        else:
            print("Opción inválida")
main()
