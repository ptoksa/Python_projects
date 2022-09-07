# Finds the total of a sequence of numbers entered by user 
def find_sum(): 
     total, iterationCount = 0, 0 # multiple assignment
     entry = input("Enter a value, or q to quit: ") 
     while entry != "q": 
         iterationCount += 1
         total += int(entry) 
         entry = input("Enter a value, or q to quit: ") 
     print ("The total is", total)
     print ("Total numbers:", iterationCount)
find_sum()