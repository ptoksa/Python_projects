def kaikki_vaarinpain(lista: list):
    tulos = ""
    for i in lista:
        tulos = i + tulos
    return tulos
if __name__ == "__main__":
    lista2 = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    print(kaikki_vaarinpain(lista2))
    kaikki_vaarinpain(lista2)
