nimi = "Teppo Testaaja"
ika = 20
taito1 = "python"
taso1 = "aloittelija"
taito2 = "java"
taso2 = "veteraani"
taito3 = "ohjelmointi"
taso3 = "puoliammattilainen"
ala = 2000
yla = 3000

print(f"nimeni on {nimi}, olen {ika}-vuotias")
print("")
print("taitoihini kuuluvat")
print(f" - {taito1} ({taso1})")
print(f" - {taito2} ({taso2})")
print(f" - {taito3} ({taso3})")
print("")
print(f"haen työtä, josta maksetaan palkkaa {ala}-{yla} euroa kuussa")

x = 4
y = 9

summa = (x + y)
print(f"27 + 15 = {summa}")
erotus = (x - y)
print(f"27 - 15 = {erotus}")
kertolasku = (x * y)
print(f"27 * 15 = {kertolasku}")
jakolasku = (x / y)
print(f"27 / 15 = {jakolasku}")

print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)

luku = int(input("Anna luku: "))

print(f"Kun kerrotaan {luku} luvulla 5, saadaan {luku * 5}")

