def viiva(leveys, mjono):
    eka = leveys * mjono
    toka = leveys * "*"
    kokki = leveys * "x"
    nekki = leveys * "X"
    vikki = leveys * "<"
    kukki = leveys * ":"
    sekki = leveys * "#"
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
    elif mjono == "#":
        print(sekki)
    else:
        print(eka)
def risulaatikko(mjono):
    leveys = 10
    #korkeus = 0
    kerrat = 0
    while kerrat < mjono:
        #viiva(leveys)
        print("#" * leveys)
        kerrat += 1
if __name__ == "__main__":
    viiva(7, "%")
    viiva(10, "LOL")
    viiva(3, "")
    viiva(5, ":-)")
    #print("#" * leveys)
    #viiva(10, "#")
    risulaatikko(2)
