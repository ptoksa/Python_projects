kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")
 
if kirjain1 > kirjain2 and kirjain1 > kirjain3:
    if kirjain2 > kirjain3:
        keski = kirjain2
    else:
        keski = kirjain3
elif kirjain2 > kirjain3:
    if kirjain3 > kirjain1:
        keski = kirjain3
    else:
        keski = kirjain1
else:
    if kirjain2 > kirjain1:
        keski = kirjain2
    else:
        keski = kirjain1
 
print("Keskimmäinen kirjain on " + keski)