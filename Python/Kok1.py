def kaikki_vaarinpain(mjono: str):
    uusi_mjono = []
    for kirjain in mjono:
            uusi_mjono = kirjain + uusi_mjono
    return uusi_mjono
if __name__ == "__main__":
    print(kaikki_vaarinpain(["Moi", "kaikki", "esimerkki", "vielä yksi"]))
    kaikki_vaarinpain(["Moi", "kaikki", "esimerkki", "vielä yksi"])
