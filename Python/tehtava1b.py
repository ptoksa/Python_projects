yht = 0
summa = 0
merkkijono = input("Anna merkkijono, Enter lopettaa: ")
while merkkijono != "":
    pituus = len(merkkijono)
    yht += pituus
    summa += 1
    merkkijono = input("Anna merkkijono, Enter lopettaa: ")
    max = 0 
    #yleisin = "" # lauseessa välit
    count = [0] * 256 
    for merkki in merkkijono : count[ord(merkki)] += 1
    for merkki in merkkijono :
        if(count[ord(merkki)] > max):
            max = count[ord(merkki)] 
            yleisin = merkki
keskiarvo = yht/summa
print("Merkkijonoja yhteensä:",summa)
print("Merkkijonon keskimääräinen pituus:",keskiarvo)
print("Merkkijonojen yleisin merkki:",yleisin)