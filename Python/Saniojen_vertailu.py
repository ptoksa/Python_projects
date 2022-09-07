a = input("Anna ensimmäinen sana: ")
b = input("Anna toinen sana: ")
if len(a) !=  len(b):            # match the length first
    print ("Sanat eivät ole samat")
else:
    count = 0                    #declare it outside of while loop
    while count < len(a):        #loop until count < length of strings
        if a[count] != b[count]:
            print ("Sanat eivät ole samat")
            break
        count = count + 1
    else:
       print ("Sanat ovat samat!")