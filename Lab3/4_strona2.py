#Zadanie czwarte z części drugiej
import random

a = random.randint(3,7)
b = random.randint(3,7)

zbior_X = set()

for i in range(a):
    zbior_X.add(random.randint(0,10))

zbior_Y = set()

for i in range(b):
    zbior_Y.add(random.randint(0,10))

print(f"Zbiór X:  {zbior_X}")
print(f"Zbiór Y:  {zbior_Y}")

#a
print(f"Czy zbiór X zawiera liczbę 5? {5 in zbior_X}")


#b
print(f"Czy zbiór X jest podzbiorem zbioru Y? {zbior_X.issubset(zbior_Y)}")


#c
print(f"Czy zbiór Y jest podzbiorem zbioru X? {zbior_Y.issubset(zbior_X)}")


#d
print(f"Czy zbiór X jest nadzbiorem zbioru Y? {zbior_X.issuperset(zbior_Y)}")


#e
print(f"Czy zbiór Y jest nadzbiorem zbioru X? {zbior_Y.issuperset(zbior_X)}")


#f
#print(f"Suma zbiorów X i Y to: {zbior_X | zbior_Y}")
print(f"Suma zbiorów X i Y to: {zbior_X.union(zbior_Y)}")


#g
print(f"Różnica zbiorów X i Y to: {zbior_X.difference(zbior_Y)}")


#h
print(f"Różnica zbiorów Y i X to: {zbior_Y - zbior_X}")


#i
#print(f"Iloczyn zbiorów X i Y to: {zbior_X & zbior_Y}")
print(f"Iloczyn zbiorów X i Y to: {zbior_X.intersection(zbior_Y)}")


#j
#print(f"Różnica symetryczna zbiorów X i Y to: {zbior_X ^ zbior_Y}")
print(f"Różnica symetryczna zbiorów X i Y to: {zbior_X.symmetric_difference(zbior_Y)}")


#k
print(f"Najwyższy element w zbiorach: {max(zbior_X.union(zbior_Y))}")


#l
pierwszy_element_X = zbior_X.pop()
zbior_Y.add(pierwszy_element_X)
#print(zbior_Y)


#m
zbior_Y.update(zbior_X)
#print(zbior_Y)


#n
zbior_X.clear()
zbior_Y.clear()
#print(zbior_X)
#print(zbior_Y)