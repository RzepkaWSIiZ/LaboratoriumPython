#Zadanie 9

import random


zakres_start = int(input("Podaj początek zakresu losowania: "))
zakres_end = int(input("Podaj koniec zakresu losowania: "))


liczba_do_zgadniecia = random.randint(zakres_start, zakres_end)


proby = 3

print(f"Zgadnij liczbę z zakresu {zakres_start} do {zakres_end}.")

for proba in range(proby):
    zgadnij = int(input(f"Próba {proba + 1}. Zgadnij liczbę: "))

    if zgadnij == liczba_do_zgadniecia:
        print(f"Brawo zgadłeś liczba to {liczba_do_zgadniecia}.")
        break
    elif zgadnij < liczba_do_zgadniecia:
        print("Za mało.")
    else:
        print("Za dużo.")
else:
    print(f"Nie udało ci się liczba to {liczba_do_zgadniecia}.")

