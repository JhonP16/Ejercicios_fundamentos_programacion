#En Medellín, las tarifas de taxi consisten en una tarifa base de $6.300 pesos colombianos, 
# más $100 por cada 56 metros recorridos. 
#Escribe una función que tome la distancia recorrida (en kilómetros) como único parámetro 
# y devuelva la tarifa total sin centavos o decimales como único resultado. 
#Escriba un programa principal que demuestre la función.

### FUNCIÓN ###

def taximetro(distancia):
    tarifa_base = 6300 #(1x100)/56 -----> dinero por cada metro
    for i in range(0, int(distancia), 1):
        tarifa_base = tarifa_base+(100/56)
    return round(tarifa_base//1)

### PROGRAMA PRINCIPAL ###

distancia = float(input("Ingrese la distancia recorrida en km "))
distancia*= 1000
print("La tarifa total fue", taximetro(distancia))