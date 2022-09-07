#Toisen asteen yhtälön ratkaiseminen
#print(sqrt(9))
#from math import sqrt

#a = int(input("Anna a: "))
#b = int(input("Anna b: "))
#c = int(input("Anna c: "))

#x = (-b + sqrt(b**2-4*a*c))/(2 * a)
#x2 = (-b - sqrt(b**2-4*a*c))/(2 * a)
#print(f"Juuret ovat {x} ja {x2}")

#Korjaa virheet
luku = int(input("Anna luku: "))
if luku < 100:
    print(f"{luku} taitaa olla onnenlukuni!")
    print("Hyvää päivänjatkoa!")
else: 
    luku > 100
    print("Luku oli suurempi kuin sata")
    print("Nyt luvun arvo on pienentynyt sadalla")
    print(f"Arvo on nyt {luku - 100}")
    print(f"{luku - 100} taitaa olla onnenlukuni!")
    print("Hyvää päivänjatkoa!")
