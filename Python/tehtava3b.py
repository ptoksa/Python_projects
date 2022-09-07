lista = [1,1,1]
def muunna(lista, funktio):
    lista()
    funktio()
def lisaa_yksi(luku):
    return luku + 1
lisatty = muunna(lista, lisaa_yksi)
print(lisatty) # Tulostaa: [2,2,2]
