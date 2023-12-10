#Zadanie 4

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

while a <= b:
    if a % 2 != 0:
        a += 1
        continue

    print(a,end=" ")
    a += 1