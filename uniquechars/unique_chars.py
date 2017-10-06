# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

# text = "anagram"
# text = list(text)
# print(text)
# print(text.count('a'))

def unique_characters(string):
    unique_letters = []
    string = list(string)
    for letter in string:
        if string.count(letter) == 1:
            unique_letters.append(letter)
    return unique_letters

# print(unique_characters("anagram"))
