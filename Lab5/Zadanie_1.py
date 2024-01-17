import random

#Zadanie 1

#a)
print(f"Dzisiejszy szczęśliwy numerek to: {random.randint(1,11)}")


#b)
roczniki = ["1996","1998","2001","2002","2003","2004"]

print(f"Szczęsliwy rocznik to: {random.choice(roczniki)}")

#c)
lista = list(range(1,50))

wylosowane_liczby = random.sample(lista,6)

print(f"Wygrywające liczby lotto to: {wylosowane_liczby}")
