def sponge_case(sentence):
    # Write your solution here!
    #split the sentence into a list of words
    #loop through each word in the list
    #loop through each char in the word.
    # if index of the char is even, lowercase this char,else upper case the char
    #join the words and return the string
    word_list = sentence.split() 
    result = []
    for word in word_list:
        new_char = ""
        for index, char in enumerate(word):
            if index % 2 == 0:
                new_char += char.lower()
            else:
                new_char += char.upper()
        result.append(new_char)

    return " ".join(result)
        




# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")