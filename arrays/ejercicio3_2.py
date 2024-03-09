cantidad_usuarios = int(input("Ingrese la cantidad de usuarios: "))

nombres = []
apellidos = []
contador_nombres = []
contador_apellidos = []
lista_nombres = []
lista_apellidos = []

contador = 0

while contador < cantidad_usuarios:
  nombre = str(input("Ingrese el nombre: "))
  apellido = str(input("Ingrese el apellido: "))
  print("------------------------------------------------------------------")

  if lista_nombres.count(nombre) == 0 and nombre != "":
    nombres.append(nombre)
    contador_nombres.append(1)
  else:
    posicion_nombre = nombres.index(nombre)
    contador_nombres[posicion_nombre]+=1
  lista_nombres.append(nombre)

  if lista_apellidos.count(apellido) == 0 and apellido != "":
    apellidos.append(apellido)
    contador_apellidos.append(1)
  else:
    posicion_apellido = apellidos.index(apellido)
    contador_apellidos[posicion_apellido]+=1
  lista_apellidos.append(apellido)

  contador+= 1

mayor_nombres = max(contador_nombres)
ind = contador_nombres.index(mayor_nombres)
nombres[ind]
mayor_apellidos = max(contador_apellidos)
ind_2 = contador_apellidos.index(mayor_apellidos)
apellidos[ind_2]

print(f"El nombre que más se repite es: {nombres[ind]}, repitiendose {mayor_nombres} veces")
print(f"El apellido que más se repite es: {apellidos[ind_2]}, repitiendose {mayor_apellidos} veces")