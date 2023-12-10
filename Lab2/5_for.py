#Zadanie 5 for

n = int(input("Podaj liczbę naturalną n: "))

if n < 0:
    print("Podana liczba nie jest naturalna.")
else:
    silnia = 1
    for i in range(1, n + 1):
        silnia *= i

    print(f"Silnia z {n} to: {silnia}")
