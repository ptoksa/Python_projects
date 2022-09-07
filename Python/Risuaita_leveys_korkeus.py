leveys = int(input("Leveys: "))
korkeus = int(input("Korkeus: "))
i = 0
while(i < korkeus):
    j = 0
    while(j < leveys):
        print('#', end = '')
        j = j + 1
    i = i + 1
    print()