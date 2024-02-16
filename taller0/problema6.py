import math

### ENTRADA ###

cateto1 = float(input("Ingrese el valor del cateto 1"))

cateto2 = float(input("Ingrese el valor del cateto 2"))

### PROCESAMIENTO ###

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

### SALIDA ###

print(f"La hipotenusa del triángulo es {hipotenusa}")


