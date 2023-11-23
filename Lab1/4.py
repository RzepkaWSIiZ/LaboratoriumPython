import math

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
c = int(input('Podaj współczynnik c: '))

delta = (b**2)-4*a*c
print(f'Delta wynosi: {delta}')

print(f'x1 wynosi: {(-b - math.sqrt(delta)) / 2*a }')
print(f'x2 wynosi: {(-b + math.sqrt(delta)) / 2*a }')



