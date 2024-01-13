#Zadanie 1
import math

def pole_kola(r):
    if r < 0:
        print("Promień koła nie może być ujemny.")
    else:
        print(f"Pole koła wynosi: {math.pi * r**2}")

pole_kola(4)

pole_kola(-70)

