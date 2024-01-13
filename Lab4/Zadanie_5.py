#Zadanie 5

def BMI(waga,wzrost):
    bmi = waga / (wzrost ** 2)
    if bmi < 16:
        print(f"Twoje BMI wynosi {bmi} (poniżej 16) - wygłodzenie.")
    elif  16 <= bmi < 16.99:
        print(f"Twoje BMI wynosi {bmi} (16 - 16.99) - wychudzenie.")
    elif 17 <= bmi < 18.49:
        print(f"Twoje BMI wynosi {bmi} (17 - 18.49) - niedowaga.")
    elif 18.5 <= bmi < 24.99:
        print(f"Twoje BMI wynosi {bmi} (18.5 - 24.99) - waga prawidłowa.")
    elif 25 <= bmi < 29.9:
        print(f"Twoje BMI wynosi {bmi} (25.0 - 29.9) - masz nadwagę.")
    else:
        print(f"Twoje BMI wynosi {bmi} (powyżej 30) masz otyłość.")


BMI(70,1.73)
