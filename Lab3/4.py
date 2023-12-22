#Zadanie czwarte z częsci pierwszej

#a
imie = str(input("Podaj imię: "))
print(f"Witaj {imie}")

#b
wiek = int(input("Podaj swój wiek: "))
print(f"Twój wiek to: {wiek}")

#c
nazwisko = str(input("Podaj swoje nazwisko: "))
print(imie[0])
print(nazwisko[0])

#d
lancuch = str(input("Podaj łańcuch: "))
print(lancuch * 5)

#e
lancuch2 = str(input("Podaj drugi łańcuch: "))
lancuch3 = lancuch+lancuch2
print(lancuch3)

#f
polowa_lancucha1 = lancuch[:len(lancuch)//2]
polowa_lancucha2 = lancuch2[len(lancuch2)//2:]

zlaczony_lancuch = polowa_lancucha1+polowa_lancucha2
print(zlaczony_lancuch)