#Lukujen käsittelyä
a = 0
laskuri = 0
positiivinen_luku = 0
negatiivinen_luku = 0
print("Syötä kokonaislukuja, 0 lopettaa: ")
while True:
    numero = input("Luku: ")
    if numero == "0":
        break
    numero = float(numero)
    a += numero
    laskuri += 1
    if numero > 0:
        positiivinen_luku += 1
    if numero < 0:
        negatiivinen_luku += 1
print(f"Lukuja yhteensä {laskuri}")
print(f"Lukujen summa {a}")
print(f"Lukujen keskiarvo {a/laskuri}")
print(f"Positiivisia {positiivinen_luku}")
print(f"Negatiivisia {negatiivinen_luku}")