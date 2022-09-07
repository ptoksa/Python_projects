yht = 0
summa = 0
merkkijono = input("Anna merkkijono, Enter lopettaa: ")
merkki={}
while merkkijono != "":
    pituus = len(merkkijono)
    yht += pituus
    summa += 1
    merkkijono = input("Anna merkkijono, Enter lopettaa: ")
    for i in merkkijono:
        if i in merkki:
            merkki[i] = merkki[i]+1
        else:
            merkki[i] = 1
yleisin= max(merkki, key = merkki.get)
keskiarvo = yht/summa
print("Merkkijonoja yhteensä:",summa)
print("Merkkijonon keskimääräinen pituus:",keskiarvo)
print("Merkkijonojen yleisin merkki:",yleisin)
