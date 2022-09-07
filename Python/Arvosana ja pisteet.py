pisteet = int(input("Anna pisteet [0-100]: "))
 
if pisteet < 0 or pisteet > 100:
    arvosana = "mahdotonta!"
elif pisteet < 50:
    arvosana = "hylätty"
elif pisteet < 60:
    arvosana = "1"
elif pisteet < 70:
    arvosana = "2"
elif pisteet < 80:
    arvosana = "3"
elif pisteet < 90:
    arvosana = "4"
else:
    arvosana = "5"
 
print(f"Arvosana: {arvosana}")
