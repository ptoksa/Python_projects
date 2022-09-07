suuruus = int(input("Lahjan suuruus: "))
 
if suuruus < 5000:
    vero = 0
elif suuruus <= 25000:
    vero = 100 + (suuruus - 5000) * 0.08
elif suuruus <= 55000:
    vero = 1700 + (suuruus - 25000) * 0.10
elif suuruus <= 200000:
    vero = 4700 + (suuruus - 55000) * 0.12
elif suuruus <= 1000000:
    vero = 22100 + (suuruus - 200000) * 0.15
else:
    vero = 142100 + (suuruus - 1000000) * 0.17
 
if vero == 0:
    print("Ei veroa!")
else:
    print(f"Vero: {vero} euroa")
