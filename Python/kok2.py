henkilo1 = {"nimi": "Pirjo Python", "pituus": 154, "paino": 61, "ikä": 44}
henkilo2 = {"nimi": "Pekka Pythonen", "pituus": 174, "paino": 103, "ikä": 31}
henkilo3 = {"nimi": "Pedro Python", "pituus": 191, "paino": 71, "ikä": 14}

henkilot = [henkilo1, henkilo2, henkilo3]

for henkilo in henkilot:
    print(henkilo["nimi"])

yhteispituus = 0
for henkilo in henkilot:
    yhteispituus += henkilo["pituus"]

print("Keskipituus on", yhteispituus / len(henkilot))
