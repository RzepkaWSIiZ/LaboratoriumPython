#Zadanie 3
#def wyswietlanie_wartosci(imie,wiek):
#    print(f"Imie: {imie}")
#    print(f"Wiek: {wiek}")

#wyswietlanie_wartosci("Norbert",60)

#a)
#def wyswietlanie_wartosci(imie,wiek):
#    """
#    Funkcja pobiera 2 parametry imie i wiek oraz wypisuje je na ekranie.
#
#    """
#    print(f"Imie: {imie}")
#    print(f"Wiek: {wiek}")
#
#
#wyswietlanie_wartosci("Norbert",60)
#
#print(wyswietlanie_wartosci.__doc__)

#b)
def wyswietlanie_wartosci(imie,wiek=20):
    """
    Funkcja pobiera 2 parametry imie i wiek oraz wypisuje je na ekranie.

    """
    print(f"Imie: {imie}")
    print(f"Wiek: {wiek}")


wyswietlanie_wartosci("Norbert")

print(wyswietlanie_wartosci.__doc__)