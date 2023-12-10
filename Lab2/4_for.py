#Zadanie 4 for


n = int(input("Podaj naturalną liczbe n ciągu: "))
a = int(input("Podaj pierwszy wyraz ciągu: "))
r = int(input("Podaj różnicę ciągu: "))

for i in range(n):
    element = a + i * r
    print(element,end=" ")
