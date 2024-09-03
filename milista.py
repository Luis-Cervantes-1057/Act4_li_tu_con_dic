# Ejemplo del uso de listas
misnovias = ["Ale", "Alesita", "Messi"]
misnum = ["10", "33", "777"]
# Mostrando a mis novias
print(misnovias)
# Mostrando mis numeros raros
print(misnum)

print ("-----accediendo a los elemetos de la lista----")
print(misnovias[1])
print(" ")
if "Ana" in misnovias:
  print("Sip, 'Alesita' es mi noviecita")
else:
  print("No eres mi chavilla")

print("Numeros de novias")
novias = len(misnovias)
print(f"Numero de novias = {novias}")

print("Ciclo for en lista")
posicion = 0
for mimujer in misnovias:
  print(posicion," ",mimujer)
  posicion = posicion+1