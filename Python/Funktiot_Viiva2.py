#Funktiot_viiva
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)
if __name__ == "__main__":
    viiva(7, "%")
    viiva(10, "LOL")
    viiva(3, "")
    viiva(5, ":-)")
    viiva (11, "xxx")
