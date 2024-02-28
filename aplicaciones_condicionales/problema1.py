# Diseñar un programa que evalúe un año cualquiera entre 0 y 5000 e indique si el año es o no bisiesto.

num = int(input("Ingrese un año entre 0 y 5000"))

### PROCESAMIENTO ###
if num >=0 and num <= 5000:
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                print(f"El año {num} es bisiesto")
            else:
                print(f"El año {num} NO es bisiesto")
        else:
            print(f"El año {num} es bisiesto")    
    else:
        print(f"El año {num} NO es bisiesto")
else:
    print("El año ingresado no está dentro de los límites establecidos")
    