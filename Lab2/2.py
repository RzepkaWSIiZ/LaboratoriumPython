#Zadanie 2

startX = -4
koniecY = 4
krok = 0.5

x = startX
while x <= koniecY:
    y = 2 * x**2 - 5 * x - 8
    print(f"{x}  {y}")
    x += krok
