#Zadanie trzecie z częsci drugiej

rachunki = {
    "Lipiec": 900,
    "Sierpień": 1100,
    "Wrzesień": 1000,
    "Październik": 777,
    "Listopad": 800
}

wartosci_rachunkow = list(rachunki.values())

#a
maksymalna_wartosc = max(wartosci_rachunkow)
print(f"Maksymalna wartość rachunku: {maksymalna_wartosc}")

minimalna_wartosc = min(wartosci_rachunkow)
print(f"Minimalna wartość rachunku: {minimalna_wartosc}")

suma_rachunkow = sum(wartosci_rachunkow)
print(f"Suma rachunku: {suma_rachunkow}")

srednia_wartosc = (suma_rachunkow / len(wartosci_rachunkow))
print(f"Średnia wartość rachunków: {srednia_wartosc}")

#b
if wartosci_rachunkow[-1] > srednia_wartosc:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")
