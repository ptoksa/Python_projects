lista = [1,1,1]                         
def muunna(lista):
    lista2 = []                        
    for numero in range(len(lista)):
        lista[numero] *= 3
        lista2 += [lista[numero]]                     
    return lista2
print(muunna(lista))
