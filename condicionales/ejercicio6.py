# Diseñe un programa que determine si un punto está dentro de la circunferencia, sobre la circunferencia o fuera de la circunferencia.

### ENTRADA ###

import math

radio = float(input("Ingrese el radio de la circunferencia"))
Cx = float(input("Ingrese la coordenada x del centro la circunferencia"))
Cy = float(input("Ingrese la coordenada y del centro la circunferencia"))
Px = float(input("Ingrese el punto x"))
Py = float(input("Ingrese el punto y"))

### PROCESAMIENTO ###

distancia = math.sqrt((Px-Cx)**2 + (Py-Cy)**2)

if distancia < radio:
    print("El punto está dentro de la circunferencia")
elif distancia == radio:
    print("El punto está sobre la circunferencia")
else:
    print("El punto está fuera de la circunferencia")

