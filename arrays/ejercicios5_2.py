cantidad_numeros  = int(input("Ingrese la cantidad de números: "))
numeros = []
pares = []

for i in range(0, cantidad_numeros, 1):
    numero = int(input("Ingrese el número:"))
    if numero % 2 == 0:
        pares.append(numero)
    numeros.append(numero)

print(f"Hay {len(pares)} números pares, los cuales son {pares}")