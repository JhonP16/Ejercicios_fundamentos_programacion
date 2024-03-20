palabra = str(input("Ingrese la palabra, por favor "))
caracteres = []

for caracter in palabra:
  caracteres.append(caracter)

intentos = 7

while intentos > 0:
  letra = str(input("Ingrese la letra, por favor "))
  for indexacion in caracteres:
    if indexacion == letra:
      print("Has acertado")
      break