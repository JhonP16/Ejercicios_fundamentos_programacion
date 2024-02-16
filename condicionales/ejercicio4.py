# En una tienda, un producto tiene descuento de 20% si su precio es mayor a $100.000. 
#Además, si el producto es de marca Sony tiene descuento adicional de 10%
#Si es de marca Panasonic tiene descuento 15%. 
#Diseñe un programa que calcule el precio total de un producto.

### ENTRADA ###

precio = float(input("Ingrese el precio del producto"))
marca = str(input("Ingrese la marca del producto"))

### PROCESAMIENTO ###

if precio > 100000:
    descuento = 0.2
else:
    descuento = 0

if marca == "sony" or marca == "Sony":
    descuento += 0.1
elif marca == "panasonic" or marca == "Panasonic":
    descuento += 0.15
else:
    descuento+= 0

### SALIDA ###

print(f"El precio total del producto es {precio - precio*descuento}")