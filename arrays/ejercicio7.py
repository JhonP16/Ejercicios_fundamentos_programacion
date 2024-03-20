# Encontrar la raíz cuadrada, el cuadrado y el cubo de un grupo de números enteros positivos.
import math

numeros = []
raices = []
cuadrados = []
cubos = []
cantidad = int(input("Ingrese la cantidad de números: "))

for index in range(0, cantidad, 1 ):
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

print(f"Los números que usted ingresó son: {numeros}")
print("---------------------------------------------------------- \n")

for num in numeros:
    raiz = math.sqrt(num)
    raices.append(raiz)
    cuadrado = num**2
    cuadrados.append(cuadrado)
    cubo = num**3
    cubos.append(cubo)

print(f"Las raíces de los números son, respectivamente \n {raices}")
print("----------------------------------------------------------")
print(f"Los cuadrados de los números son, respectivamente \n {cuadrados}")
print("----------------------------------------------------------")
print(f"Los cubos de los números son, respectivamente \n {cubos}")

