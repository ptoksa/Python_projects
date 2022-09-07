#syote = input("Anna nimi: ")
#syote2 = int(input("Anna syntymävuosi: "))
#vuosi = int(syote2)
#print(f"Moi {syote}, olet {2020 - vuosi} vuotta vanha vuoden 2020 lopussa")

#Vuorokaudet sekunteina
#luku1 = int(input("Kuinka monen vuorokauden sekunnit tulostetaan? "))
#summa = luku1 * 60 * 60 * 24
#print(f"{summa}")

#Korjaa ohjelma: Lukujen tulo
#luku1 = int(input("Anna luku 1: "))
#luku2 = int(input("Anna luku 2: "))
#luku3 = int(input("Anna luku 3: "))

#tulo = luku1 * luku2 * luku3

#print("Tulo on", tulo)

#Lukujen summa ja tulo
#luku1 = int(input("Luku 1: "))
#luku2 = int(input("Luku 2: "))

#summa = luku1 + luku2
#tulo = luku1 * luku2

#print("Lukujen summa", summa)
#print("Lukujen tulo", tulo)

#Lukujen summa ja keskiarvo
#luku1 = int(input("Luku 1: "))
#luku2 = int(input("Luku 2: "))
#luku3 = int(input("Luku 3: "))
#luku4 = int(input("Luku 4: "))

#summa = luku1 + luku2 + luku3 + luku4
#keskiarvo = (luku1 + luku2 + luku3 + luku4)/4

#print(f"Lukujen summa on {summa} ja keskiarvo {keskiarvo}")

#Ruokailukustannukset
#luku1 = int(input("Montako kertaa viikossa syöt Unicafessa? "))
#luku2 = float(input("Unicafe-lounaan hinta? "))
#luku3 = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

#keskiarvo1 = (luku1 * luku2 + luku3)/7
#keskiarvo2 = (luku1 * luku2 + luku3)
#print("")
#print(f"Kustannukset keskimäärin: ")
#print(f"Päivässä {keskiarvo1} euroa")
#print(f"Viikossa {keskiarvo2} euroa")

#Opiskelijat ryhmiin
luku1 = int(input("Montako opiskelijaa? "))
luku2 = int(input("Mikä on ryhmän koko? "))

määrä = (luku1 - 1 + luku2) // luku2
print(f"Ryhmien määrä: {määrä}")
