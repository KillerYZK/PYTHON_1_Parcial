"""Clase-3.Py
15/08/2025
 Programa para evaluar la calificación de un alumno"""

print("------------------------------------------------------")
print("Programa de evaluación de alumnos ")
print("------------------------------------------------------")
calif = int (input("caputrar calificacion: "))  
def evaluacion(calif):
    if calif > 10 or calif < 0:
        print("Calificación no válida, debe ser entre 0 y 10")
    elif calif == 11:
        print("Calificación no válida, debe ser entre 0 y 10")
    elif calif == 10 or calif == 9:
        print("Excelente con la calificación de", calif)    
    elif calif >= 6:
        print("Aprobado con la calificación de", calif)
    else:
        print("Reprobado con la calificación de %d, que horrible" % calif)
    print("------------------------------------------------------")
    print("Fin del programa")
    print("------------------------------------------------------")
evaluacion(calif)
