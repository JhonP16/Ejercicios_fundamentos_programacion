# Diseñe un programa que, dado un número, determine si el número es par o impar.

### ENTRADA ###

numero = int(input("Ingrese un número"))

### PROCESAMIENTO ###

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")