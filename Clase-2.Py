print("Programa de evaluación de alumnos")

nota_alumno = input("Introduce la nota del alumno: ")

# int() convierte cadena a número
def evaluacion(nota):
    valor = "aprobado"
    if nota < 5:
        valor = "reprobado"
    return valor

r = evaluacion(int(nota_alumno))
print("El alumno está", r)