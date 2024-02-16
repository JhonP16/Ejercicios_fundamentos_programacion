#Si una persona gana más de 3000 dólares mensuales, tal persona debe pagar un impuesto del 4% sobre el valor mensual.
#Diseñe un programa que lea el salario de una persona y determine cuanto impuesto debe pagar esa persona.

### ENTRADA ###

sueldo = float(input("Ingrese su sueldo"))

### PROCESAMIENTO ###

if sueldo > 3000:
    impuesto = sueldo*0.04
    print(f"El impuesto a pagar es {round(impuesto)}")
elif sueldo <= 3000:
    print(f"No debe pagar impuesto :)")