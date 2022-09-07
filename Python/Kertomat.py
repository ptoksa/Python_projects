while True:
    kertoma = 1
    n = 1
    numero = int(input("Anna luku: "))
    if numero <= 0:
        print("Kiitos ja moi!")
        break
    while n < numero:
        n += 1
        kertoma*=n
    print(f"Luvun {numero} kertoma on {kertoma}")
