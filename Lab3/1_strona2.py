#Zadanie pierwsze z częsci drugiej
import random
import string

n = int(input("Podaj liczbe n elementów: "))
x = int(input("Podaj długość ciągów x: "))
s = int(input("Podaj wartość s dla sprawdzenia długości ciągów: "))

lista_ciagow = []

for i in range(n):
    ciag = ""
    for i in range(x):
        ciag += random.choice(string.ascii_lowercase)
    lista_ciagow.append(ciag)

krotka = tuple(lista_ciagow)

print(krotka)

#a

ilosc_znakow = 0
for ciag in krotka:
    ilosc_znakow += len(ciag)
print(f"Ilość znaków w liście: {ilosc_znakow}")


#b
ilosc_liter_k = 0
for ciag in krotka:
    ilosc_liter_k += ciag.count('k')
print(f"Ilość liter k to: {ilosc_liter_k}")

#c
ilosc_ciagow_kt = 0
for ciag in krotka:
    ilosc_ciagow_kt += ciag.count('kt')
print(f"Ilość ciągów kt to: {ilosc_ciagow_kt}")

#d
ilosc_ciagow_dluzszych_niz_s = 0
for ciag in krotka:
    if len(ciag) > s:
        ilosc_ciagow_dluzszych_niz_s += 1
print(f"Ilość ciągów dłuższych niż {s} to {ilosc_ciagow_dluzszych_niz_s}")