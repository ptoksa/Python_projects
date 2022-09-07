import random
highest = 10

answer = random.randrange(1,highest)
guess = 0
count = 0

print("please guess a number between 1 and {}".format(highest))

while guess != answer:
    guess = int(input())
    if count == 4:
        exit(print("you exceeded number of chances"))
    if guess == answer:
        print("well done you have guessed it correctly and the answer is {}".format(guess))
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
        count = count +1
        count+=1
