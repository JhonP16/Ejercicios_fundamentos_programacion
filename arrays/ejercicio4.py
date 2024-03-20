cantidad_num = int(input("Ingrese la cantidad de numeros positivos "))
numeros = []
acumulado = 0

for i in range(0, cantidad_num, 1):
    numero = int(input("ingrese un numero "))
    numeros.append(numero)

for i in numeros:
    acumulado+= i 


promedio = acumulado/cantidad_num

print("El promedio de la lista de números es: ", promedio)
    