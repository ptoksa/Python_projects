# Moduuli laskin
# Funktio tuplaa: palauttaa parametrin "luku" kaksinkertaisena

def tuplaa(luku):
    return luku * 2

# main-funktio, jota ei kutsuta, jos joku tuo laskin-moduulin omaan ohjelmaansa
# import-käskyllä ja kutsuu tuplaa-funktiota   
def main():
    numero = int(input("Anna kokonaisluku:\n"))
    tupla = tuplaa(numero)
    print("Antamasi luku kaksinkertaisena on:", tupla)

# Kutsutaan main-funktiota vain, jos joku ajaa laskin-moduulin sellaisenaan
# Esimerkiksi avaa tiedoston Spyderiin ja ajaa koodin
if __name__ == "__main__":    
    main()
#import laskin
print("5 x 2 on:", tuplaa(5))