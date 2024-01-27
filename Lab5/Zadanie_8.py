#Zadanie 8

import math


def pole_trojkata_ostrokatnego(a, b, kat_stopnie):
    if a <= 0 or b <= 0 or kat_stopnie <= 0:
        print("Długości boków i kąt muszą być dodatnie.")

    if kat_stopnie >= 90:
        print("Trójkąt nie jest ostrokątny kąt przekracza 90 stopni.")

    kat_radiany = math.radians(kat_stopnie)

    pole = 0.5 * a * b * math.sin(kat_radiany)

    print(pole)


a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
kat = float(input("Podaj szerokość kąta ostrego pomiędzy bokami (w stopniach): "))


wynik = pole_trojkata_ostrokatnego(a, b, kat)
print(wynik)
