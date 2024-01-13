#Zadanie 8
def potega_n_a(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * potega_n_a(a, n-1)
    else:
        return 1 / (a * potega_n_a(a, -n-1))


podstawa = float(input("Podaj liczbę a: "))
wykladnik = int(input("Podaj wykładnik: "))

wynik = potega_n_a(podstawa, wykladnik)

print(f"Wynik potęgowania to {wynik}")