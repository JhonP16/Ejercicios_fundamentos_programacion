# Un automóvil soporta solo 500 kg de peso y debe transportar un número de pasajeros desconocido,
# los cuales se van subiendo uno a uno al automóvil.

#Ingrese y lea uno a uno los pasajeros en el automóvil indicando si aún hay espacio para otro pasajero.

peso_max = 500
peso_acumulado = 0
num_pasajeros = 0

while peso_acumulado <= peso_max:
    peso_pasajero = int(input("Ingrese el peso: "))
    peso_acumulado += peso_pasajero
    num_pasajeros += 1

if peso_acumulado > peso_max:             # Si el peso llega a exceder en la última iteración los 500 máximos
    print("El último pasajero excede el peso permitido, no lo podemos llevar")
    print("-----------------------------------------------------------------")
    peso_acumulado -= peso_pasajero       # Vamos a restar al peso acumulado el peso de la última persona
    num_pasajeros -= 1                    # Y restaremos ese pasajero sobrante


print(f"El número de pasajeros fueron {num_pasajeros}, sumando un total de {peso_acumulado}kg ")

