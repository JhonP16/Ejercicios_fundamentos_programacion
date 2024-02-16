# El banco de la república emite billetes de diferentes denominaciones:
#$100.000; $50.000; $20.000; $10.000; $5.000; $2000 y billetes de $1000.

#Diseñe un programa que lea una cantidad de dinero (max. $5.000.000 y min. $1000) 
#exprese esa cantidad en billetes de diferentes denominaciones.

### ENTRADA ### 
billetes_100 = 0
billetes_50 = 0
billetes_20 = 0
billetes_10 = 0
billetes_5 = 0
billetes_2 = 0
billetes_1 = 0

dinero = int(input("Ingrese la cantidad de dinero entre 1000 y 5.000.000"))

### PROCESAMIENTO

if dinero >= 1000 and dinero <=5000000:
  if dinero >=10000:
    billetes_100 = dinero//100000
    dinero = dinero % 100000
  if dinero >= 50000:
    billetes_50 = dinero//50000
    dinero = dinero % 50000
  if dinero >= 20000:
    billetes_20 = dinero//20000
    dinero = dinero % 20000
  if dinero >= 10000:
    billetes_10 = dinero//10000
    dinero = dinero % 10000
  if dinero >= 5000:
    billetes_5 = dinero//5000
    dinero = dinero % 5000
  if dinero >= 2000:
    billetes_2 = dinero//2000
    dinero = dinero % 2000
  if dinero >= 1000:
    billetes_1 = dinero//1000
    dinero = dinero % 1000

### SALIDA ###

print(f"La cantidad de billetes para la cantidad ingresada {dinero} es \n Billetes de 100.000: {billetes_100} \n Billetes de 50.000: {billetes_50} \n Billetes de 20.000: {billetes_20} \n Billetes de 10.000: {billetes_10} \n Billetes de 5.000: {billetes_5} \n Billetes de 2.000: {billetes_2} \n Billetes 1.000: {billetes_1}")




