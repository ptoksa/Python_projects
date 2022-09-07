Input_Sentence = input("Enter your sentence: ")
print(Input_Sentence)
count = 0
i=0
try:
    while (Input_Sentence[i] != "\n"):
        if (Input_Sentence[i] == ' '):
            count=count+1
            i+=1
        else:
            i+=1
except:
    count = count+1
    print ('Number of Words in a given sentence is :'      +str(count))