lista = []
while True:
    n = int(input("Anna luku (0 tai pienempi keskeyttää): "))
    if n < 1:
        break
    lista.append(n)
print(lista)
print("Listan suurin luku on", max(lista))
print("Listan pienin luku on", min(lista))
