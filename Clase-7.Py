"""
Listas
Isaac Echeverria Alvarez
27/08/2025
"""

lista5 = []

lista = ["Isaac", 4, -9, False, "Echeverria"]
lista2 = [13,2,3,7,5,11,1,25,101]
print(lista)
print(lista[0:3])
print(lista[2:])
print(lista[1:])

lista.append("Echeverria")
lista.insert(2, "Alvarez")
lista.extend(["Beach", "volleyball"])
lista2.sort() 
lista.reverse()
lista.remove(-9)
print(lista2)

for l in lista:
    print(l)

i = 0
while i < len(lista):
    print(lista[i])
    i+=1