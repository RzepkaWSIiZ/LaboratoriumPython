#Zadanie 6
def pole_trojkata(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        pole = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"Pole trójkąta o bokach wynosi: {pole}")
    else:
        print("Nie można utworzyć trójkąta o podanych bokach.")


a = float(input("Podaj bok a trójkąta: "))
b = float(input("Podaj bok b trójkąta: "))
c = float(input("Podaj bok c trójkąta: "))

pole_trojkata(a, b, c)