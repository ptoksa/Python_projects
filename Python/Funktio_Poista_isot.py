def poista_isot(mjono):
    result = []
    for merkki in mjono:
        if not merkki.isupper(): result.append(merkki)
    return (result)
if __name__ == "__main__":
    print(poista_isot(["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]))
    poista_isot(["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"])
