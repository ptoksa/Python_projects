count = 0
total = 0
average = 0 
while True:
    numlist = input('Enter a number or press Enter to quit: ')
    if numlist == '':
            break
    try:
            count = count + 1
            total = total + float(numlist)
    except:
            count = count - 1
            print('Enter a valid number')
            continue
average = float(total)/float(count) 
print('The sum is',total)
print('The average is',average)