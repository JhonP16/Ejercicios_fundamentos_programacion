# Hacer un algoritmo que encuentre la suma de los números impares comprendidos entre 1 y N.

n = int(input("ingrese hasta que N números quiere hacer la suma de impares: "))
suma = 0

for i in range(1, n+1, 2):
    suma += i

print(f"La suma de los números impares hasta N es: {suma}")
