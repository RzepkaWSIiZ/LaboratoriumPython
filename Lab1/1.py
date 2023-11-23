wiek = int(input('Wprowadź wiek klienta: '))
cena_biletu = 0

if wiek < 4:
    print('Wstęp bezpłatny :)')
elif 4 <= wiek <= 18:
    cena_biletu += 10
    print(f'Cena biletu wynosi: {cena_biletu}')
else:
    cena_biletu += 20
    print(f'Cena biletu wynosi: {cena_biletu}')




