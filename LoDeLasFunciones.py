#---
def salute():
    print("Hello!")

salute()
# ---
def say(string):
    print(f"Saying... {string}!")

say("Eooo")
# ---
def sum(a, b):
    return (a + b)
print(sum(2, 2))
print(sum(b=3,a=1))
# ---
def duality(a, b):
    return (a + b, a - b)
print(duality(5, 2))
# ---
def impuestoAplicado(precio, iva = 1.21):
    print(precio * iva)
impuestoAplicado(100)
impuestoAplicado(100, 1.25)
# ---
def variadic(*params): # si ponemos "**" no es variádico, sino que recibe un diccionario
    for val in params:
        print(val)
variadic("Muriatic", "Acid", "Caustic", "Soda")
variadic(1, 2, 3)
# ---
def forceTypeToInt(a: int) -> int: # Se especifica el tipo de retorno, que no se limita al mismo
    return("Sida")
print(forceTypeToInt(288))
# ---
def variadicOperation(operator, *values):
    result = 0
    if (operator == "+"):
        for val in values:
            result+=val
    elif (operator == "-"):
         for val in values:
            result-=val
    elif (operator == "*"):
        for val in values:
            result*=val
    elif (operator == "/"):
        for val in values:
            result/=val
    else:
        print("Wrong operator")
    print(result)
variadicOperation("+", 1, 1, 1)
variadicOperation("-", 5, 2) # esto va raro
variadicOperation("*", 5, 2) # esto va raro
variadicOperation("/", 5, 2) # esto va raro

