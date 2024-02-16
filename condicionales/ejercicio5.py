#Diseñe un programa que lea los lados A, B y C de un triángulo.
#Determine en primer lugar sí es posible formar un triángulo.
#Luego, si el triángulo es Equilátero, Isósceles o Escaleno.

### ENTRADA ###

a = float(input("Ingrese el lado A del triangulo"))
b = float(input("Ingrese el lado B del triangulo"))
c = float(input("Ingrese el lado C del triangulo"))

### PROCESAMIENTO ###

if a+b > c and a+c > b and b+c > a:
    if a == b == c:
        print("Es un triángulo Equilátero")
    elif a == b or a == c or b == c:
        print("Es un triángulo Isósceles")
    else:
        print("Es un triángulo Escaleno")
else:
    print("No es un triángulo")