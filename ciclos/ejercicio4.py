# ¿El siguiente programa que valor imprime?

total = 21
x = 7

while True:
    x += 2
    if x % 5 == 0:
        continue
    elif x % 7 == 0:
        break
    total += x
print(total)
print(x)