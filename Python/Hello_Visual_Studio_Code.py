while True:
    editori = input("Editori: ")
    if editori.lower() == "visual studio code":
        break
    if editori.lower() == "word" or editori.lower() == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")
print("loistava valinta!")
