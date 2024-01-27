#Zadanie 7

import random
import math

poczatek = int(input("Podaj początek zakresu: "))
koniec = int(input("Podaj koniec zakresu: "))

krotka = tuple(random.randint(poczatek, koniec) for i in range(10))

print(f"Wylosowana krotka: {krotka}")

iloczyn = 1
for element in krotka:
    iloczyn *= element

srednia_geo = math.pow(iloczyn, 1/len(krotka))


print(f"Średnia geometryczna krotki: {srednia_geo}")