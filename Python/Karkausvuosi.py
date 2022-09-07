vuosi = int(input("Anna vuosi: "))
 
# Oletetaan aluksi, että ei ole karkausvuosi
karkausvuosi = False
 
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        karkausvuosi = True
elif vuosi % 4 == 0:
    karkausvuosi = True
 
if karkausvuosi:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
