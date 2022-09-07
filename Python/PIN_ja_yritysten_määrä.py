yrityksia = 1
while True:
    pin = input("PIN-koodi: ")
    if pin == "4321":
        break
    print("Väärin")
    yrityksia += 1
 
if yrityksia == 1:  
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yrityksia} yritystä")
