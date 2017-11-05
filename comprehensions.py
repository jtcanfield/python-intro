wordslist = ["File", "apple", "directory", "bannana"]

def reverseword(word):
    return word[::-1]

for word in wordslist:
        print(reverseword(word))

reversed_words = []
for word in wordslist:
        reversed_words.append(reverseword(word))
print(reversed_words)

reversed_words = [reverseword(word) for word in wordslist]
word_lengths = [len(word) for word in wordslist]
new_word_list = [word for word in wordslist]

short_word_list = [word for word in wordslist if len(word) < 7]
print ("short words: ", short_word_list)


# JS
"""
words.map(function (x, i)=>{
    return word.reverse()
})
"""
