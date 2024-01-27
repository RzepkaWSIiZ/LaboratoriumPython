#Zadanie 10

from datetime import datetime, timedelta

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))


data = datetime(rok, miesiac, dzien)

#a)
dzien_roku = data.timetuple().tm_yday

#b)
numer_tygodnia = data.isocalendar()[1]

#c)
data_przed = data - timedelta(days=14)
data_po = data + timedelta(days=14)

#d)
dni_do_niedzieli = (6 - data.weekday()) % 7
data_niedzieli = data + timedelta(days=dni_do_niedzieli)

#e)
czas_unixowy = int((data - datetime(1970, 1, 1)).total_seconds())


print("a. Dzień roku:", dzien_roku)
print("b. Numer tygodnia:", numer_tygodnia)
print("c. Daty na 2 tygodnie przed i po:")
print("   Przed:", data_przed.strftime("%Y-%m-%d"))
print("   Po:", data_po.strftime("%Y-%m-%d"))
print("d. Data najbliższej niedzieli:", data_niedzieli.strftime("%Y-%m-%d"))
print("e. Czas unixowy bieżącej godziny w podanym dniu:", czas_unixowy)