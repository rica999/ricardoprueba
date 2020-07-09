# Ejercicio que determine si un estudiante esta aprobado o no
# Autor: Ricardo

def determinaraprobado(promedio):
    if int(promedio)>=11:
        resultado="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado

promedio = input ("Promedio: ")
print (determinaraprobado(promedio))
