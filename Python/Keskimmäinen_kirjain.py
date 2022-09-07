k1 = input("Anna 1. kirjain: ")
k2 = input("Anna 2. kirjain: ")
k3 = input("Anna 3. kirjain: ")

if k1 > k2 and k1 > k3:
    keskimmäinen = k1
    if k2 > k3 and k2 > k3:
        keskimmäinen = k2
    else:
        keskimmäinen = k3
elif k1 < k2 and k1 < k3:
    keskimmäinen = k1
    if k2 < k3 and k2 < k3:
        keskimmäinen = k2
    else:
        keskimmäinen = k3
elif k1 > k2 and k3 > k2:
    keskimmäinen = k1
elif k1 < k2 and k1 > k3:
    keskimmäinen = k1
print(f"Keskimmäinen kirjain on {keskimmäinen}")
