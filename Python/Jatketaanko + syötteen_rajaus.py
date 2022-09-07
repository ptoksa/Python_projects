#Jatketaanko
#while True:    
#    print(f"moi")
#    jatketaanko = input("Jatketaanko? ")
#    if jatketaanko == "ei":
#        break
#print("ei sitten")

#Syötteen rajaus
from math import sqrt
while True:
    luku = int(input("Syötä luku: "))
    if luku < 0:
        print(f"Epäkelpo luku")
        continue
    if luku == 0:
        print(f"Lopetetaan...")
        break
    print(sqrt(luku))


