def viiva(leveys, mjono):
    eka = leveys * mjono
    toka = leveys * "*"
    kokki = leveys * "x"
    nekki = leveys * "X"
    vikki = leveys * "<"
    kukki = leveys * ":"
    if mjono == "":
        print(toka)
    elif mjono >= "x":
        print(kokki)
    elif mjono >= "X":
        print(nekki)
    elif mjono == "<3":
        print(vikki)
    elif mjono == ":-)":
        print(kukki)
    else:
        print(eka)
if __name__ == "__main__":
    viiva(7, "%")
    viiva(10, "LOL")
    viiva(3, "")
    viiva(5, ":-)")
