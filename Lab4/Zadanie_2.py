#Zadanie 2
def pole_trapezu(a,b,h):
    if a < 0 or b < 0 or h < 0:
        print("Wymiary trapezu nie mogą być ujemne.")
    else:
        pole = int((a+b)*h/2)
        print(f"Pole trapezu wynosi: {pole}")

pole_trapezu(-2,4,2)

pole_trapezu(4,2,2)


