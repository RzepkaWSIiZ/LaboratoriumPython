litera = input('Wprowadź literę a program zgadnie czy jest duża czy mala: ')

if litera.isalpha():
    if litera.islower():
        print(f'Wprowadzona litera {litera} jest mała!')
    elif litera.isupper():
        print(f'Wprowadzona litera {litera} jest duża!')
else:
    print(f'{litera} To nie jest litera')
