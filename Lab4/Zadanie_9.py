#Zadanie 9
def fibonacci(n):
    if n <= 0:
        print("Podaj liczbę naturalną która jest większa od zera.")
    elif n == 1:
        print("0")
    elif n == 2:
        print("1")
    else:
        fib_1 = 0
        fib_2 = 1
        for i in range(2, n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(f"{n}ty wyraz ciągu Fibonacciego to: {fib_2}")


nr_wyrazu = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))
fibonacci(nr_wyrazu)
