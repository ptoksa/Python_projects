numInput = int(input("Multiplication using value? : "))
num = 1
while num <= numInput:
    i = 1
    while i <= numInput:
        product = num*i
        print(num, "X", i, "=", product)
        i = i + 1
    print("")
    num = num + 1