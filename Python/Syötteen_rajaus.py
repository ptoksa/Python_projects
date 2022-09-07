from math import sqrt
while True:
    luku = int(input("luku: "))
    if luku == 0:
        break
    if luku > 0:
        print(sqrt(luku))
    else:
        print("Epäkelpo luku")
        
print("Lopetetaan...")
