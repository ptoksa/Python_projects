#Orwell
#vuosiluku = int(input("Anna luku: "))

#if vuosiluku == 1984:
#    print("Orwell")

#Itseisarvo
#luku = int(input("Anna luku: "))

#if luku < 0:
 #   luku = luku * -1
  #  print(f"Luvun itseisarvo on {luku}")

#else:
 #   print(f"Luvun itseisarvo on {luku}")

#Keittoa vai ei
#nimi = input("Mikä on nimesi: ")
#if nimi == "Jerry":
#    print(f"Seuraava!")
#else:
#    annos = int(input("Kuinka monta annosta keittoa: "))
#    print(f"Kokonaishinta on {annos * 5.90}")
#    print(f"Seuraava!")

#Luvun suuruusluokka
#luku = int(input("Anna luku: "))
#if luku == 1123:
#    print(f"Kiitos!")
#elif luku < 10:
#    print(f"Luku on pienempi kuin 1000")
#    print(f"Luku on pienempi kuin 100")
#    print(f"Luku on pienempi kuin 10")
#    print(f"Kiitos!")
#elif luku < 100:
#    print(f"Luku on pienempi kuin 1000")
#    print(f"Luku on pienempi kuin 100")
#    print(f"Kiitos!")
#elif luku < 1000:
#    print(f"Luku on pienempi kuin 1000")
#    print(f"Kiitos!")
#else:
#    print(f"Kiitos!")

#Laskin
luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
komento = input("Komento: ")

summa = (luku1 + luku2)
tulo = (luku1 * luku2)
erotus = (luku1 - luku2)

if komento == "summa":
    print("")
    print(f"{luku1} + {luku2} = {summa}")
if komento == "tulo":
    print("")
    print(f"{luku1} * {luku2} = {tulo}")
if komento == "erotus":
    print("")
    print(f"{luku1} - {luku2} = {erotus}")
