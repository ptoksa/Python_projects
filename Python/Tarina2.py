#Tarina
tarina = ""
edellinen_sana = None
while True: 
    sana = input("Anna sana: ")
    if sana == "loppu":
        break
    if edellinen_sana == sana:
        break
    edellinen_sana = sana
    tarina += sana + " "
print(tarina)
