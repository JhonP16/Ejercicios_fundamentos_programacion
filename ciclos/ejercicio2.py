# Escriba las tablas de multiplicar del número 1 al N, y cada tabla del 1 al M.

tabla = int(input("Ingrese la cantidad de tablas que desea ver "))
num = int(input("Ingrese hasta que número desea multiplicar en cada tabla "))

for tabla in range(1, tabla+1, 1):
    for contador in range(1, num+1, 1):
        print(f"{tabla} x {contador} = {tabla*contador}")
    print("------------------------------------------------------------------------------")