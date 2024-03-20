cantidad_numeros  = int(input("Ingrese la cantidad de números: "))
numeros = []
contador_pares = 0

for i in range(0, cantidad_numeros, 1):
    numero = int(input("Ingrese el número:"))
    numeros.append(numero)

for index in numeros:
    if index %2 == 0:
        contador_pares += 1

print(f"Hay {contador_pares} números pares")
