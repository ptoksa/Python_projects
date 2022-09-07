yht = 0
summa = 0
r = 1
merkkijono = input("Anna merkkijono, Enter lopettaa: ")
for merkki in merkkijono:
    p = merkkijono.count(merkki)
    if p > r:
        r = p
        s = merkki
while merkkijono != "":
    pituus = len(merkkijono)
    yht += pituus
    summa += 1
    merkkijono = input("Anna merkkijono, Enter lopettaa: ")
keskiarvo = yht/summa
print("Merkkijonoja yhteensä:",summa)
print("Merkkijonon keskimääräinen pituus:",keskiarvo)
print("Merkkijonojen yleisin merkki:",s)
