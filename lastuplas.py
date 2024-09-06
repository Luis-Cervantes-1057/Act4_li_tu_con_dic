# Ejemplo de usar Tuplas
arcoiris = ("Azul", "Verde", "Rojo", "Amarillo")
print(arcoiris)
print(" ")
print("-- Longitud de arcoiris --")
print(len(arcoiris))
print(" ")

animales = ("Pantera", 20, " Estatura", 1.7)
print(animales)
print(" Elementos de la Tupla ")
print(animales[0])
print(" ")

rateros = ("Juan", "Emiliano", "Paola")
y = list(rateros)
y[0] = "Edgar"
x = tuple(y)

print(x)
print(" ")
print("Agregando elementos")
Nanimal = ("ElMen", "Chetos")
y = list(Nanimal)
print(y)
y.append("Duquesa")
otratuple = tuple(y)
print(otratuple)
print(" ")

print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)