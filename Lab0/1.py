
"""
Zadanie 1

type(1+2)      ---> <class 'int'>
type(1+4.5)    ---> <class 'float'>
type(3/2)      ---> <class 'float'>
type(4/2)      ---> <class 'float'>
type(3//2)     ---> <class 'int'>
type(-3//2)    ---> <class 'int'>
type(11%2)     ---> <class 'int'>
type(2**10)    ---> <class 'int'>
type(8**(1/3)) ---> <class 'float'>


Zadanie 2

int(3.0)    ---> 3
float(3.0)  ---> 3.0
float("3")  ---> 3.0
str(12.4)   ---> '12.4'
bool(0)     ---> False
"""
#Zadanie 3

a = int(input('Proszę podać bok a prostokąta: '))
b = int(input('Proszę podać bok b prostokąta: '))

print(f'Pole prostokąta wynosi: {a*b}')
print(f'Obwód prostokąta wynosi: {2*a + 2*b}')

#Zadanie 4.0

droga = float(input('Podaj droge pokonaną przez samochodód w km: '))
spalanie = float(input('Podaj spalanie samochodu l/100km: '))

cena_paliwa = 6.5

zuzycie_paliwa = (spalanie/100)*droga
print(f'Przewidywane zużycie paliwa: {zuzycie_paliwa}')
print(f'Szacowany koszt podróży wynosi {cena_paliwa*zuzycie_paliwa}')


import random
#Zadanie 4.1

droga = random.randint(1,100000)
spalanie = float(input('Podaj spalanie samochodu l/100km: '))

cena_paliwa = 6.5

zuzycie_paliwa = (spalanie/100)*droga
print(f'Przewidywane zużycie paliwa: {zuzycie_paliwa}')
print(f'Szacowany koszt podróży wynosi {cena_paliwa*zuzycie_paliwa}')

#Zadanie 5


#3 edit
a = int(input('Proszę podać bok a prostokąta: '))
b = int(input('Proszę podać bok b prostokąta: '))

print(f'Pole prostokąta wynosi: {a*b}')
print(f'Obwód prostokąta wynosi: {2*a + 2*b}')

#4 edit
droga = random.randint(1,100000)
spalanie = float(input('Podaj spalanie samochodu l/100km: '))

cena_paliwa = 6.5

zuzycie_paliwa = (spalanie/100)*droga
print(f'Przewidywane zużycie paliwa: {zuzycie_paliwa}')
print(f'Szacowany koszt podróży wynosi {cena_paliwa*zuzycie_paliwa}')
