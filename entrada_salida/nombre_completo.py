# 1. Leer 4 entradas del usuario: primer nombre; segundo nombre; primer apellido y segundo apellido
# 2. Concatenar las variables String
# 3. Imprimir el nombre completo

### ENTRADA ###

nombre1 = str(input("Ingrese el primer nombre"))

nombre2 = str(input("Ingrese el segundo nombre"))

apellido1 = str(input("Ingrese el primer apellido"))

apellido2 = str(input("Ingrese el segundo apellido"))

### PROCESAMIENTO ###

nombre_completo = nombre1 + " " + nombre2 + " " + apellido1 + " " + apellido2

### SALIDA ###

print(f"El nombre completo es {nombre_completo}")
