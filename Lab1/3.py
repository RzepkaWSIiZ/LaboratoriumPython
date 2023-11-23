print('Jaką opercaję chcesz wykonać?')
print('1) dodawanie')
print('2) odejmowanie')
print('3) mnożenie')
print('4) dzielenie ')
print('5) potęgowanie ')

operacja = int(input('Wpisz numer operacji: '))

a = int(input('Podaj argument 1: '))
b = int(input('Podaj argument 2: '))


if operacja == 1:
    print(f'Wynik: {a+b}')
elif operacja == 2:
    print(f'Wynik: {a-b}')
elif operacja == 3:
    print(f'Wynik: {a*b}')
elif operacja == 4:
    print(f'Wynik: {a/b}')
elif operacja == 5:
    print(f'Wynik: {a**b}')
else:
    print(f'Podano niewłaściwy numer operacji: {operacja}')
