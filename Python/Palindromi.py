def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]
n = input("Anna sana: ")
if n == reverse(n):
    print ("Palindromi")
else:
    print ("Ei palindromi")
