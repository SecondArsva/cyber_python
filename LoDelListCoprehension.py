# Ejemplos avanzados
colores = ["rojo", "verde", "azul"]
tallas = ["Small", "Medium", "Long"]
new = [(color, talla) for color in colores for talla in tallas]
print(f"LstA: {colores}")
print(f"LstB: {tallas}")
print(f"New: {new}")

# 0. A partir de una lista de compresión, crear una nueva lista a partir de dos listas dadas


# 1. Aplanar una matriz
print("--- Aplanar matriz ---")
matrix = [[1,2,3], [4,5,6], [7,8,9]]
single = [element for lane in matrix for element in lane]
print(f"Matriz: {matrix}")
print(f"Lista plana: {single}")


# Crear una matriz identidad donde 1.1 2.2 3.3 4.4 ... tengas los mismos valores
print("--- Matriz identidad ---")
length = int(input("Introduce un numerito para determinar la longitud de la matriz identidad: "))
ident = [element for lane in range(0, length + 1) for element in range(0, length + 1) if (lane == length)]
print(ident)

# convertir grados celsius y convertimos a farehneig * 9 / 100 + 32???

# Extraer vocales de una cadena
print("--- Extraer vocales ---")
string = "Hola, amigos del Youtube"
new = [char for char in string.lower() if char in "aáeéiíoóuú"]
print(f"Cadena: {string}")
print(f"Vocales: {new}")