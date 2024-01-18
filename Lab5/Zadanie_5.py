#Zadanie 5

import keyword

def sprawdz_keyword(k):
    if keyword.iskeyword(k):
        print(f"{k} jest keywordem.")
    else:
        print(f"{k} nie jest keywordem.")


sprawdz_keyword("for")
sprawdz_keyword("print")
sprawdz_keyword("break")
sprawdz_keyword("done")
sprawdz_keyword("bad")