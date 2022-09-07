def poista_isot(merkkijonot: list):
    ilman_isoja = []
    for merkkijono in merkkijonot:
        if not merkkijono.isupper():
            ilman_isoja.append(merkkijono)
    return ilman_isoja
if __name__ == "__main__":
    print(poista_isot(["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]))
    poista_isot(["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"])
