#funciones
"""
para comentar una línea se usa el símbolo #
para comentar varias líneas se usa comillas triples
"""

numerico = 10
precio = 10.5
texto = "Hola, Python"
flag = True or False
producto = "coca cola"  

def ventas(precio, cantidad):
    iva = 0.16
    total = precio * cantidad * (1 + iva)  
    return total

print("El precio del producto es:", precio)
print("El producto es:", producto)
print("El total de la venta es:", ventas(precio, 2))