#Salasana uudelleen
salasana1 = input("Salasana: ")
salasana2 = input("Toista salasana: ")
while True:
    if salasana1 != salasana2:
        print("Ei ollut sama!")
        salasana2 = input("Toista salasana: ")
    if salasana1 == salasana2:
        break   
print("Käyttäjätunnus luotu!")

#Salasana uudelleen
salasana = input("Salasana: ")
while True:
    salasana_uudelleen = input("Toista salasana: ")
    if salasana == salasana_uudelleen:
        break
    print("Ei ollut sama!")
 
print("Käyttäjätunnus luotu!")