wordslist = ["File", "apple", "directory", "bannana"]

# Lets say we want to reverse a bunch of words.

# We could make a reverse word method...
def reverseword(word):
    return word[::-1]

# ...and use a loop to print the word and put it in an array
reversed_words = []
for word in wordslist:
    reversed_words.append(reverseword(word))
#     print(reverseword(word))
# print(reversed_words)


# OR we could use comprehensions!
# inside of the brackets, the whitespace does not matter
reversed_words = [reverseword(word) for word in wordslist]
word_lengths = [len(word) for word in wordslist]
new_word_list = [word for word in wordslist]
short_word_list = [word for word in wordslist if len(word) < 7]
print(reversed_words)
print(word_lengths)
print(new_word_list)
print ("short words: ", short_word_list)


# JS
"""
words.map(function (x, i)=>{
    return word.reverse()
})
"""
