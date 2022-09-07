def ilman_vokaaleja(mjono):
    mjono2 = mjono
    vokaalit = ("a", "e", "i", "o", "u", "y", "ä", "ö", "å")
    for i in mjono.lower():
        if i in vokaalit:
            mjono2 = mjono2.replace(i,"")
    return mjono2
if __name__ == "__main__":
    mjono = "abcdefghijklmnopqrstuvwxyzåäö"
    print(ilman_vokaaleja(mjono))
