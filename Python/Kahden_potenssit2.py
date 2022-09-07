#Kahden potenssit
numero = int(input("Mihin asti: "))
exponentti = 0
while 2 ** exponentti <= numero:
    print(2 ** exponentti) 
    exponentti = exponentti + 1
