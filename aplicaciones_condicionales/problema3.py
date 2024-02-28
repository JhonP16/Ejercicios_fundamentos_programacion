# Diseñar un programa que lea: La hora, los minutos y la jornada (mañana o tarde) y retorne la cantidad de minutos que faltan para las 12 am (midnight)
# Ejemplo: ENTRADA => hora: 11,  minutos: 55,  jornada: pm. SALIDA => faltan 5 minutos para las 12 am (midnight).
# ENTRADA => hora: 12, minutos: 0, jornada: pm. SALIDA => faltan 720 minutos para las 12 am (midnight).
# ENTRADA => hora: 9, minutos: 10, jornada: pm. SALIDA => faltan 170 minutos para las 12 am (midnight).

### ENTRADA ###

hora = int(input("Ingrese la hora"))
minutos = int(input("Ingrese los minutos"))
jornada = input("Ingrese la jornada (am o pm)")

### PROCESAMIENTO ###

if hora == 12:
    hora = 0

hora_transformada = hora*60

if jornada == "am" or jornada == "AM":
    minutos_pa_12 = 1440 - (hora_transformada+minutos)
    print(f"faltan {minutos_pa_12} pa las 12")
else:
    minutos_pa_12 = 720 - (hora_transformada+minutos)
    print(f"faltan {minutos_pa_12} minutos pa las 12")