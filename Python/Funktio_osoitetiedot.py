# osoitetiedot.py
def tee_osoite():
    print("Anna seuraavan henkilon tiedot.")
    etunimi = input("Etunimi: ")
    sukunimi = input("Sukunimi: ")
    katuosoite = input("Katuosoite: ")
    postinumero = input("Postinumero: ")
    postitoimipaikka = input("Postitoimipaikka: ")
    osoite = etunimi + " " + sukunimi + "\n" + katuosoite + "\n" + \
        postinumero + " " + postitoimipaikka.upper()
    return osoite

def main():
    print("Talla ohjelmalla voit syottaa ja tulostaa osoitteita.")
    osoitteet = []
    jatko = True
    while jatko:
        uusi_osoite = tee_osoite()
        osoitteet.append(uusi_osoite)
        vastaus = input("Haluatko antaa lisaa osoitteita (k/e)?\n")
        if vastaus.lower() == "e":
            jatko = False
    print
    print("Antamasi osoitteet:")
    for osoitetieto in osoitteet:
        print(osoitetieto)
        print
main()