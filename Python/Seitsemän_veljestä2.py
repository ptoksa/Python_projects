#Seitsemän veljestä
def seitseman_veljesta():
    nimet = "Tuomas Eero Aapo Juhani Lauri Simeoni Timo"
    n = nimet.split(" ")
    n = sorted(n)
    print("\n".join(n))  
if __name__ == "__main__":
    seitseman_veljesta()
