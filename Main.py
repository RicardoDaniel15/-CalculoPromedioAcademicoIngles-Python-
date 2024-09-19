"""
Este programa permite calcular el promedio final de un ciclo academico en el CEC

Las PONDERACIONES con las que se trabaja son:

Pruebas:
1era Prueba -- 10%
2da  Prueba -- 15%
3era Prueba -- 20%
4era Prueba -- 35%
Total Pruebas: 80/100

Participacion en clase:
Total Participación: 10%

Examen Oral:
Total Oral Examen: 10%

Encuenta Instructor:
Total extra: 2%

El RESULTADO DEL CURSO dependera de las asistencias totales:
Más de 8 faltas -- 73/100
Menos de 8 o 8  -- 83/100

Nota:
Se realiza una resta de 1.84 a la ponderacion final dado a la tendencia de fallo que se encontro con las operaciones, es decir,
puede existir un margen de error de hasta 0.5 decimales
@author: Ricardo
"""

print("*************************************************Bienvenido*************************************************")
print("Este programa permitira calcular el promedio del ciclo academico")
print("* Ponderacion PRUEBAS: ")
try:
    prueba1 = float(input("Ingrese la nota de la 1ª Prueba (0-100): "))
    prueba2 = float(input("Ingrese la nota de la 2ª Prueba (0-100): "))
    prueba3 = float(input("Ingrese la nota de la 3ª Prueba (0-100): "))
    prueba4 = float(input("Ingrese la nota de la 4ª Prueba (0-100): "))
    participacion = float(input("Ingrese el porcentaje de sus participaciones en clase (0-10): "))
    oralExam = float(input("Ingrese el porcentaje del Examen Oral (0-10): "))
    asistencias = int(input("Digite cuantas ausencias tuve este ciclo academico: "))

    # Validación de rango para pruebas
    if not all(0 <= nota <= 100 for nota in [prueba1, prueba2, prueba3, prueba4]):
        raise ValueError("ERROR!! Las notas de las pruebas deben estar entre 0 y 100.")

    # Validación de rango para participación y examen oral
    if not all(0 <= nota <= 10 for nota in [participacion, oralExam]):
        raise ValueError("ERROR!! Las notas de la participación y examen oral deben estar entre 0 y 10.")

    extra = bool(int(input("¿Lleno la encuesta de instructores? (1 para sí, 0 para no): ")))
    if extra==True:
        porcentajeExtra = 2
    elif extra==False:
        porcentajeExtra = 0

    totalPruebas = (prueba1*0.1) + (prueba2*0.15) + (prueba3*0.2) + (prueba4*0.35)
    ponderacionFinal = totalPruebas + participacion + oralExam + porcentajeExtra - 1.84

    print(f"PONDERACIONES: \n1era Prueba: {prueba1}\n2nd Prueba: {prueba2}\n3era Prueba: {prueba3}\n4era Prueba: {prueba4}\n"
          f"Ponderacion Pruebas 80/100 = {totalPruebas}")
    print(f"Ponderacion participaciones en clase: {participacion}\nPonderacion Examen Oral: {oralExam}\nPonderacion extra: {porcentajeExtra}")

    if ponderacionFinal>=73 and asistencias<=8:
        print(f"FELICIDADES!! Usted paso el ciclo con un promedio de {ponderacionFinal}")
    elif ponderacionFinal>=83 and asistencias>=9:
        print(f"FELICIDADES!! Usted paso el ciclo con un promedio de {ponderacionFinal}")
    else:
        print("USTED FALLO EL CICLO ACADEMICO")

except ValueError as e:
    print(f"Error: {e}")