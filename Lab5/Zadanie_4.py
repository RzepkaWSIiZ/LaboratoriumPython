#Zadanie 4

import datetime

laby = datetime.datetime(2024,1,14)

dzis = datetime.datetime.now()

dni_od_labow = (dzis-laby).days

kolos = datetime.datetime(2024,2,11)

dni_do_kolosa = (kolos-dzis).days

print(f"Ilość dni od ostatnich laboratoriów ({laby.strftime('%d %B %Y')}): {dni_od_labow} dni")
print(f"Czas do kolokwium ({kolos.strftime('%d %B %Y')}): {dni_do_kolosa} dni")