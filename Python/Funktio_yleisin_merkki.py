# Most frequent Character
def most_frequent(a_string):
    # Create a string of symbols to exclude from counting.
    symbols = ' ,.-/?'
    characters = []
    characters_count = []
    # Check each individual character in the string.
    for ch in a_string:
        # Check that the character is not one of the symbols.
        if ch not in symbols:
            # If its not and we haven't seen it already, 
            # append it to the characters list.
            if ch not in characters:
                characters.append(ch)
                # And in the same index in the characters_count list
                characters_count.append(1)
            else:
                # If it is in the characters list, find its index
                # and add 1 to the same index at characters_count
                position = characters.index(ch)
                characters_count[position] = characters_count[position] + 1
    # find the largest value in the character_count list, it's index
    # and show the character at the same index at the characters list.
    print(characters[characters_count.index(max(characters_count))])
def main():
    # Get a string from the user.
    text = input('Give me some text and I will find you the most frequent character: ')
    most_frequent(text)

# Call main
main()
