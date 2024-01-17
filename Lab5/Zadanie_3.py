#Zadanie 3

import time

sekundy = int(input("Aby rozpocząć działanie sekundnika wpisz liczbe sekund: "))

while sekundy > 0:
    print(f"Do końca pozostało {sekundy} sekund")
    time.sleep(1)
    sekundy -= 1

print("Koniec")