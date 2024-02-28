# La única forma de saber que se tiene la hora actual, es un reloj análogo que se ve a través de un espejo, por lo tanto, la hora que se observa es un reflejo invertido de la hora real
# Diseñar un programa que reciba como entrada la hora reflejada e imprima la hora real. Los minutos menores a 10 se manejan con un solo digito
# El usuario debe ingresar la hora y minutos reflejados y el algoritmo deberá imprimir la hora y minutos reales.

# Ejemplo: ENTRADA => hora: 3, minutos: 25. SALIDA => hora_real: 8, minutos_real: 35.
# ENTRADA => hora: 9, minutos: 0. SALIDA => hora_real: 3, minutos_real: 0.

#Nótese que: 
# 1. Cuando es una hora en punto, los minutos reales siguen siendo 0 y simplemente se le resta 12 a la hora reflejada
# 2. Cuando es una hora en cualquier minuto, se le resta 11 a la hora reflejada y 60 a los minutos reflejados.

### ENTRADA ###

hora_reflejada = int(input("Ingrese la hora reflejada"))
minutos_reflejados = int(input("Ingrese los minutos reflejados"))

### PROCESAMIENTO ###

if hora_reflejada == 12: #Esto se hace con el objetivo de que no hayan problemas al poner el 12 como entrada,
    hora_reflejada = 0  #Pues con nuestro sistema horario pueden haber problemas


if minutos_reflejados == 0:
    hora_real = 12-hora_reflejada
    minutos_real = 0
else:
    hora_real = 11-hora_reflejada
    minutos_real = 60-minutos_reflejados

 
if hora_real == 0:  # Esto se hace para que en la salida no se muestre el 12 como 0,
    hora_real = 12  # Que se usó de esa manera para el procesamiento

### SALIDA ###
    
print(f"La hora real es {hora_real}:{minutos_real}")
