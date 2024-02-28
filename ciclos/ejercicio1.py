# Indicar los números que son múltiplos del 6, desde el 1 hasta el 1000.

for contador in range(6, 1000, 1):
    if contador % 6 == 0:
        print(contador)

#for contador in range(6, 1000, 6):
    #print(contador)