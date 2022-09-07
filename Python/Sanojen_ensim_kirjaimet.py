lause = input("Anna lause: ")
sanat = lause.split()
kirjaimet = [sanat[0] for sanat in sanat]
print("\n".join(kirjaimet))

lause = input("Anna lause: ")
 
# Lisätään alkuun välilyönti, jotta käsittely helpottuu
lause = " " + lause
 
# Etsitään kohdat, joita ennen on välilyönti
kohta = 1
while kohta < len(lause):
    if lause[kohta-1] == " " and lause[kohta] != " ":
        print(lause[kohta])
    kohta += 1