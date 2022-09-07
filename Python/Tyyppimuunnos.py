#sana = "abcd"
#print(len(sana))

#print(len("moikka"))

#sana2 = "heipparallaa"
#pituus = len(sana2)
#print(pituus)

#tyhja_merkkijono = ""
#pituus = len(tyhja_merkkijono)
#print(pituus)

#Merkkien määrä
#sana = input("Anna sana: ")
#if len(sana) > 1:
#    print(f"Sanassa {sana} on {len(sana)} kirjainta")
#    print(f"Kiitos!")
#if len(sana) <= 1:
#    print(f"Kiitos!")

#Tyyppimuunnos
luku = float(input("Anna luku: "))
if luku > 10:
    print("Kokonaisosa:", int(luku))
    print(f"Desimaaliosa: {float(luku) - int(luku)}")
elif luku > 1:
    print("Kokonaisosa:", int(luku))
    print(f"Desimaaliosa: {luku - 1}")
elif luku < 1:
    print("Kokonaisosa:", int(luku))
    print(f"Desimaaliosa: {luku}")




