#Korjaa ohjelma: Korkoa kortille
#pisteet = int(input("Kuinka paljon pisteitä? "))
#if pisteet < 100:
#    pisteet *= 1.1
#    print(f"Sait 10 % bonusta")
#else:
#    pisteet >= 100
#    pisteet *= 1.15
#    print(f"Sait 15 % bonusta")

#print("Pisteitä on nyt", pisteet)

#Huomiset vaatteet
print("Kerro huominen sääennuste: ")
lämpötila = int(input("Lämpötila: "))
sade = input("Sataako (kyllä/ei): ")

if lämpötila > 20 and sade == "ei":
    print(f"Pue housut ja t-paita")
elif lämpötila > 20 and sade == "kyllä":
        print(f"Pue housut ja t-paita")
        print(f"Muista sateenvarjo!")
elif lämpötila > 10 <= 20 and sade == "ei":
    print(f"Pue housut ja t-paita")
    print(f"Ota myös pitkähihainen paita")
elif lämpötila > 10 <= 20 and sade == "kyllä":
        print(f"Pue housut ja t-paita")
        print(f"Ota myös pitkähihainen paita")
        print(f"Muista sateenvarjo!")
elif lämpötila > 5 <= 10 and sade == "ei":
    print(f"Pue housut ja t-paita")
    print(f"Ota myös pitkähihainen paita")
    print(f"Pue päälle takki")
elif lämpötila > 5 <= 10 and sade == "kyllä":
        print(f"Pue housut ja t-paita")
        print(f"Ota myös pitkähihainen paita")
        print(f"Pue päälle takki")
        print(f"Muista sateenvarjo!")
elif lämpötila <= 5 and sade == "ei":
    print(f"Pue housut ja t-paita")
    print(f"Ota myös pitkähihainen paita")
    print(f"Pue päälle takki")
    print(f"Suosittelen lämmintä takkia")
    print(f"Kannattaa ottaa myös hanskat")
elif lämpötila <= 5 and sade == "kyllä":
        print(f"Pue housut ja t-paita")
        print(f"Ota myös pitkähihainen paita")
        print(f"Pue päälle takki")
        print(f"Suosittelen lämmintä takkia")
        print(f"Kannattaa ottaa myös hanskat")
        print(f"Muista sateenvarjo!")
