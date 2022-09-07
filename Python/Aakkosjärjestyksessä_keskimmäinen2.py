#Aakkosjärjestyksessä keskimmäinen
k1 = input("Anna 1. kirjain: ")
k2 = input("Anna 2. kirjain: ")
k3 = input("Anna 3. kirjain: ")

if k1 > k2 and k1 > k3:
    suurin = k1
elif k2 > k3 and k2 > k3:
    suurin = k2
else:
    suurin = k3
print(f"Keskimmäinen kirjain on {suurin}")
