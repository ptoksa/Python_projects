def henkilotiedot():
    sanakirjan_avaimet = ['ika', 'nimi', 'pituus']
    lista = []
    while True:
        henkilotieto = {}
        for avain in sanakirjan_avaimet:
            tiedot = input(f"Syötä {avain}, Enter lopettaa: ")
            if tiedot == "":
                return lista
            henkilotieto[avain] = tiedot
        lista.append(henkilotieto)
henkilotiedot = henkilotiedot()
print(henkilotiedot)
