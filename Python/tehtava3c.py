lista = [1,1,1,1]
def lisää_yksi(lista2):
    for numero in range(len(lista2)):
        lista2[numero] += 1
    return lista2
print(lisää_yksi(lista))
