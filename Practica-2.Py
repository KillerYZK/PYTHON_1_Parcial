""" 
Metodos de cadena
Isaac Echeverría Álvarez
02/09/2025
"""

import os
import time

"""Voy a solicitar ya sea una frase o un refran al usuario para despues seperar las palabras, 
hacerla mayusculas, contar cuantas veces aparece y remplazar la palabra que se quiera
"""
def clear():
    os.system('cls')

print ("------------------------------------")
print ("|Introduce una frase:              |")
print ("------------------------------------")
frase = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()


#Usar el metodo split para separar las palabras de la frase 

print ("------------------------------------")
print ("| Separar las palabras de la frase |")
print ("------------------------------------")
m_split = frase
print (m_split.split())
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()

#Usar el metodo upper para poner la frase en mayusculas
print ("------------------------------------")
print ("|      Frase en mayusculas         |")
print ("------------------------------------")
m_upper = frase 
print (m_upper.upper())
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()

#Usar el metodo count para contar cuantas veces aparece una palabra en la frase
print ("------------------------------------")
print ("|Cuantas veces se repite la palabra|")
print ("------------------------------------")
print ("|Selecciona una palabra de la frase|")
print ("------------------------------------")
print (frase)
m_palabra = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()
print ("------------------------------------")
m_count = frase
m_count.count(m_palabra)
print ("La palabra", m_palabra, "se repite", m_count.count(m_palabra), "veces")
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
print (frase)
m_palabra2 = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()
print ("------------------------------------")
print ("| escribe la palabra por la que la |")
print ("|          quieres remplazar       |")

m_palabra3 = input()
print ("------------------------------------")
input("Presiona Enter para continuar...")
clear()
print ("------------------------------------")
m_replace = frase
print (m_replace.replace(m_palabra2, m_palabra3))
print ("------------------------------------")
