# Diseñar un programa que evalúe un año cualquiera entre 0 y 5000 e indique si el año es o no bisiesto.
# SOLUCIÓN ALTERNATIVA

### ENTRADA ###

num = int(input("Ingrese un año entre 0 y 5000"))

### PROCESAMIENTO ###
if num >=0 and num <= 5000:
    if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
        print(f"El año {num} es bisiesto")
    else:
        print(f"El año {num} No es bisiesto")
else:
    print(f"El año {num} no está dentro de los límites establecidos")