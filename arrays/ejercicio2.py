#En una maratón los corredores van llegando a la meta, y se va marcando el tiempo en minutos. 
#Diseñe un programa que lea y almacene los tiempos de los corredores hasta que se ingrese 0.
#Finalmente, se imprima el ganador, y quienes quedaron por encima del tiempo límite 330 minutos.


### ENTRADA ###
descalificados = []
tiempos= []
tiempo = float(input("Ingrese el tiempo: "))

while tiempo > 0:
    tiempos.append(tiempo)

    if tiempo > 330:
        descalificados.append(tiempo)
    
    tiempo = float(input("Ingrese el tiempo: "))

tiempos.sort()

print(f"El ganador tuvo un tiempo de {tiempos[0]} minutos")
print(f"Los descalificados fueron en total {len(descalificados)} con tiempos de {descalificados}")