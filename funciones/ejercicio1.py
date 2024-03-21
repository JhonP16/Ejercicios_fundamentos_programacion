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
                mediana = (numeros[0] + numeros[1]) / 2
                mediana = round(mediana)
                return mediana
            else:
                numeros.pop(-1)
                numeros.pop(0)
    
### PROGRAMA PRINCIPAL ###
lista_numeros = []

while True:
    numero = int(input("Ingrese el número: "))
    if numero == -1:
        break
    else:
        lista_numeros.append(numero)

print("La mediana es ", mediana(lista_numeros))

        
