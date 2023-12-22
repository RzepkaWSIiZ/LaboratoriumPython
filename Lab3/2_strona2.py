#Zadanie drugie z częsci drugiej

lista_zakupow = {
    "ser": 4.50,
    "jaja": 12.50,
    "woda": 3.50,
    "ketchup": 11.00
}
print(lista_zakupow)

for artykuł, kwota in lista_zakupow.items():
    print(f"{artykuł}: {kwota} zł")

suma_wydatkow = sum(lista_zakupow.values())
print(f"Suma wydatków to: {suma_wydatkow}")