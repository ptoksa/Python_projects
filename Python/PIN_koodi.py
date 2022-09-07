yritykset = 0
ei_onnistunut = 0
onnistui = 0
while True:
    tunnus = input("PIN-koodi: ")
    yritykset += 1
    if tunnus != "4321":
        ei_onnistunut = True
        print("Väärin")
    if tunnus == "4321":
        onnistui = True
        break
if ei_onnistunut:
    print(f"Oikein, tarvitsit {yritykset} yritystä")
elif onnistui:
    print("Oikein, tarvitsit vain yhden yrityksen!")
        
    