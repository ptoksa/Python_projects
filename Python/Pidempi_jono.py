#Pidempi jono
#mjono1 = input("Anna jono 1: ")
#mjono2 = input("Anna jono 2: ")
#if len(mjono1) > len(mjono2):
#    print(f"{mjono1} on pidempi")
#elif len(mjono1) == len(mjono2):
#    print(f"Jonot ovat yhtä pitkät")
#else:
#    print(f"{mjono2} on pidempi")

#jono1 = input("Anna jono 1: ")
#jono2 = input("Anna jono 2: ")
 
#if len(jono1) > len(jono2):
#    print(jono1, "on pidempi")
#elif len(jono2) > len(jono1):
#    print(jono2, "on pidempi")
#else:
#    print("Jonot ovat yhtä pitkät")

#Lopusta alkuun
mjono = input("Anna merkkijono: ")
kohta = len(mjono) - 1
while kohta >= 0:
    print(mjono[kohta])
    kohta -= 1

mjono = input("Anna merkkijono: ")
indeksi = -1
while indeksi >= -len(mjono):
    print(mjono[indeksi])
    indeksi -= 1