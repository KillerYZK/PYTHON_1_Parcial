"""
Metodos para cadenas
Isaac Echeverria Alvarez
27/08/2025
"""
# Metodos para cadenas
cadena1 = "soraya"
print("capitalize", cadena1.capitalize())

cadena2 = "SoS"
print("casefold", cadena2.casefold())
print("center", cadena2.center(10, '*'))

menus = ["Menu ATM", "1. Ingresar dinero", "2. Retirar dinero", "3. Consultar saldo", "4. Salir"]
for menu in menus:
    print(menu.center(30, '-'))

cadena3 = "Don quixote de la mancha"
print("count", cadena3.count("o",1,30))
