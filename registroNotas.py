indice = 0
total = 0
cantAprobados = 0
cantReprobados = 0
totalEstudiantes = int(input("Digite el numero de estudiantes a evaluar: "))
while indice < totalEstudiantes:
    calificacion = float(input("Digite la nota del estudiante: "))
    if calificacion < 0 or calificacion > 5.0:
        print("Nota no valida")
    else:
        if calificacion >= 3.0:
            print("Aprobado")
            cantAprobados = cantAprobados + 1
        else:
            print("Reprobado")
            cantReprobados = cantReprobados + 1
    indice = indice + 1
    total = total + calificacion
media = total / totalEstudiantes
print("El numero de estudiantes evaluados fueron:", totalEstudiantes)
print("Aprobados:", cantAprobados)
print("Reprobados:", cantReprobados)
print("Promedio:", media)
