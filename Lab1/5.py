x = int(input('Podaj liczbe x: '))
y = int(input('Podaj liczbe y: '))
z = int(input('Podaj liczbe z: '))

if x > y:
    x, y = y, x
if y > z:
    x, y, z = x, z, y
if x > y:
    x, y = y, x

print(f'Uporządkowane liczby: {x} {y} {z}')
