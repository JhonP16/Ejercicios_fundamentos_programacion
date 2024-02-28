# Diseñe un algoritmo en Lenguaje Python que tomando como entrada la fecha de cumpleaños arroje el signo zodiacal del usuario. 
#La entrada serán dos números enteros, el primero será el día del mes y el segundo será el mes en el año. La salida deberá mostrar el signo zodiacal delusuario.

### ENTRADA ###

dia = int(input("Ingrese su día de nacimiento"))
mes = int(input("Ingrese su mes de nacimiento"))

### PROCESAMIENTO ###
if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12):
    if mes == 1 and (dia >=1 and dia <=20):
        print("Usted es Capricornio")
    if mes== 1 and (dia >= 21 and dia <= 31):
        print("Usted es Acuario")
    if(mes == 2 and (dia >=1 and dia <= 19)):
        print("Usted es Acuario")
    if mes == 2 and (dia >=20 and dia <=31):
        print("Usted es Piscis")
    if mes == 3 and (dia >=1 and dia <= 20):
        print("Usted es Piscis")
    if mes == 3 and (dia >=21 and dia <= 31):
        print("Ustes es Aries")
    if mes == 4 and (dia >=1 and dia <= 20):
        print("Usted es Aries")
    if mes == 4 and (dia >=21 and dia <= 31):
        print("Usted es Tauro")
    if mes == 5 and (dia >=1 and dia <= 20):
        print("Usted es Tauro")
    if mes == 5 and (dia >=21 and dia <= 31):
        print("Usted es Géminis")
    if mes == 6 and (dia >=1 and dia <= 21):
        print("Usted es Géminis")
    if mes == 6 and (dia >=22 and dia <= 31):
        print("Usted es Cáncer")
    if mes == 7 and (dia >=1 and dia <= 22):
        print("Usted es Cáncer")
    if mes == 7 and (dia >=23 and dia <=31):
        print("Usted es Leo")
    if mes == 8 and (dia >=1 and dia <=23):
        print("Usted es Leo")
    if mes == 8 and (dia >=24 and dia <=31):
        print("Usted es Virgo")
    if mes == 9 and (dia >=1 and dia <=22):
        print("Usted es Virgo")
    if mes == 9 and (dia >=23 and dia <=31):
        print("Usted es Libra")
    if mes == 10 and (dia >=1 and dia <=22):
        print("Usted es Libra")
    if mes == 10 and (dia >=23 and dia <=31):
        print("Usted es Escorpio")
    if mes == 11 and (dia >=1 and dia <=22):
        print("Usted es Escorpio")
    if mes == 11 and (dia >=23 and dia <=31):
        print("Usted es Sagitario")
    if mes == 12 and (dia >=1 and dia <=21):
        print("Usted es Sagitario")
    if mes == 12 and (dia >=22 and dia <=31):
        print("Usted es Capricornio")
else:
    print("Ingresa una fecha valida :)")

    

