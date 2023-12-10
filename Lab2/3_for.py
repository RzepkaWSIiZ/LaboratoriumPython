#Zadanie 3 for


# a)
#h = int(input("Podaj wysokość choinki: "))

#for i in range(1,h + 1):
#    print("* "*i)

# b)

h = int(input("Podaj wysokość choinki: "))
for i in range(1,h + 1):
    odstępy = " " * (h-i)
    gwiazdki = "* "* i
    print(odstępy+gwiazdki)