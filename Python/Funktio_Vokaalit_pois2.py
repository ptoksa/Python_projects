def ilman_vokaaleja(mjono: str):
    vokaalit = "aeiouyåäö"
    tulos = ""
    for kirjain in mjono:
        if kirjain not in vokaalit:
            tulos += kirjain
    return tulos
if __name__ == "__main__":
    mjono = "abcdkfdåådädääd"
    print(ilman_vokaaleja(mjono))
