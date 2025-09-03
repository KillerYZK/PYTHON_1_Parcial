""" 
Metodos de cadena
Isaac Echeverría Álvarez
02/09/2025
"""

import os

"""
Voy a solicitar ya sea una frase o un refran al usuario para despues seperar las palabras, 
hacerla mayusculas, contar cuantas veces aparece y remplazar la palabra que se quiera

"""
def clear():
    os.system('cls')

#introducir frase
print ("------------------------------------")
print ("|Introduce una frase:              |")
print ("------------------------------------")
frase = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()


#Usar el metodo split para separar las palabras de la frase y guardarlas en el arreglo

print ("------------------------------------")
print ("| Separar las palabras de la frase |")
print ("------------------------------------")
lista = []
for palabra in frase.split():
    palabra_centrada = palabra.center(40)
    lista.append(palabra_centrada)
    print(palabra_centrada)

print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()

# Convertir a mayúsculas y mostrar
print ("------------------------------------")
print ("|      Frase en mayusculas         |")
print ("------------------------------------")
lista_u = [palabra.upper() for palabra in frase.split()]
for palabra in lista_u:
    print(palabra.center(40))


#Usar el metodo count para contar cuantas veces aparece una palabra en la frase
print ("------------------------------------")
print ("|Cuantas veces se repite la palabra|")
print ("------------------------------------")
print ("|Selecciona una palabra de la frase|")
print ("------------------------------------")
print (lista_u)
m_palabra = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()
print ("------------------------------------")
conteo = frase.count(m_palabra)
print(f"La palabra '{m_palabra}' se repite {conteo} veces")
print ("------------------------------------")
if m_palabra not in frase:
    print ("La palabra no se encuentra en la frase")
    print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()

#Usar el metodo replace para remplazar una palabra por otra
print ("------------------------------------")
print ("|  Remplazar una palabra por otra  |")
print ("------------------------------------")
print ("|Selecciona una palabra de la frase|")
print ("------------------------------------")
print (lista_u)
m_palabra2 = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()
print("------------------------------------")
print("| escribe la palabra por la que la |")
print("|          quieres remplazar       |")
print("------------------------------------")
m_palabra3 = input()
print("------------------------------------")
input("Presiona Enter para continuar...")
clear()

# Reemplazar palabra
frase_nueva = frase.replace(m_palabra2, m_palabra3)

# Mostrar frase modificada en formato vertical y centrado
print("------------------------------------")
print("|     Frase modificada centrada    |")
print("------------------------------------")
lista_nueva = ""
for palabra in frase_nueva.split():
    linea = palabra.upper().center(40)
    lista_nueva += linea + "\n"
    print(linea)
print("------------------------------------")


