while True:
    editori = input("Editori: ")
    if editori.lower() == "visual studio code":
        break
    if editori == "word" or editori == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")
print("loistava valinta!")