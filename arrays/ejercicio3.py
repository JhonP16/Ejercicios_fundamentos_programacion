#Un curso de fundamentos de programación tiene 102 estudiantes con sus nombres y apellidos. 
#Diseñe un programa que encuentre cuál es el nombre más común y la cantidad de ocurrencias, 
#y cuál es el apellido más común y la cantidad de ocurrencias a partir de la siguiente lista:

### ENTRADA ###

nombres = ["JUAN", "MARIA", "PEDRO", "MARIA", "JUAN", "MARIA", "ANA", "PEDRO", "MARIA"]

contador = {}
for nombre in nombres:
    if nombre in contador:
        contador[nombre] +=1
    else:
        contador[nombre] = 1
    
nombre_mas_comun = None
ocurrencias = 0

for nombre, cantidad in contador.items():
    if cantidad > ocurrencias:
        nombre_mas_comun = nombre
        ocurrencias = cantidad

print(f"El nombre más común es {nombre_mas_comun} con {ocurrencias} ocurrencias")







