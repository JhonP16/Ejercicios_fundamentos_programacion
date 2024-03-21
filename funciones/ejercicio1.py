#Escriba una función que reciba una lista de números como parámetro y devuelva el valor de mediana de la lista de números.
#Incluya un programa principal que lea los valores mientras no se ingrese -1, y finalmente muestre su mediana.

### FUNCIÓN ###
def mediana(numeros):
    numeros.sort()
    if len(numeros) % 2 != 0:
        for index in range(0, len(numeros), 1):
            if len(numeros) == 1:
                mediana = numeros[0]
                return mediana
            else:
                numeros.pop(-1)
                numeros.pop(0)
    elif len(numeros) % 2 == 0:
        for index in range(0, len(numeros), 1):
            if len(numeros) == 2:
                mediana = (numeros[index - 1] + numeros[index]) / 2
                return mediana
            else:
                numeros.pop(-1)
                numeros.pop(0)
    
### PROCESAMIENTO ###
cantidad_numeros = int(input("Ingrese la cantidad de números: "))
lista_numeros = []

for i in range(0, cantidad_numeros, 1):
    numero = int(input("Ingrese el número: "))
    lista_numeros.append(numero)

print("La mediana es ", mediana(lista_numeros))

        
