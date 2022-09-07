lista = [1, 2, 3, 4, 5]
while True:
    indeksi = int(input("Anna indeksi: "))
    arvo = input("Anna arvo: ")        
    if indeksi == 0:
        arvo = lista[0]
    if indeksi == 1:
        indeksi = []
    
    if indeksi == -1 or arvo == -1:
        break
print(lista)