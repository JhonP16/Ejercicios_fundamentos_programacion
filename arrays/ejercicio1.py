# Un usuario introduce la cantidad N de números enteros, seguido por los N números enteros, uno por uno. 
#Diseñe un programa en Python que guarde e imprima una lista con los cuadrados de todos los enteros.

### ENTRADA ###
n = int(input("Ingrese el número de cuadrados"))
cuadrados = []

### PROCESAMIENTO ###

for i in range(0, n, 1):
    numero = int(input("Ingrese el número: "))
    numero_cuadrado = numero**2
    cuadrados.append(numero_cuadrado)

### SALIDA ###
print(cuadrados)
              