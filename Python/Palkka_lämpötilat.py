#Lämpötilat
#syöte = int(input("Anna lämpötila (F): "))

#lämpötila = (syöte - 32)/1.8
#print(f"{syöte} fahrenheit-astetta on {lämpötila} celsius-astetta")
#if lämpötila < 0:
#   print(f"Paleltaa!")

#Palkka
syöte1 = float(input("Tuntipalkka: "))
syöte2 = float(input("Työtunnit: "))
syöte3 = input("Viikonpäivä: ")

Palkka = (syöte1 * syöte2)
if syöte3 == "sunnuntai":
    print(f"Palkka {Palkka *2} euroa")
else:
    syöte3 == "maanantai" or "tiistai" or "keskiviikko" or "torstai" or "perjantai" or "lauantai"
    print(f"Palkka {Palkka} euroa")

