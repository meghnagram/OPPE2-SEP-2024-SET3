def get_words_after_the(sentence: str) -> list:
    
    words = sentence.split()
    words_after_the = []
    for i in range(1, len(words)):
       if words[i - 1].lower() == 'the':
           words_after_the.append(words[i])
    return words_after_the

# #Another method
# def get_words_after_the(sentence: str) -> list:
#     l=[]
#     m=[]
#     l=sentence.split(' ')
#     pre=l[0]
    
#     for i in range(1,len(l)):
#         if pre.lower() == 'the':
#             m.append(l[i])
#         pre=l[i]
            
#     return m


# Get Words That Come After "the"
# Write a function to find all the words that immediately follow the word "the" in a given sentence. The search should be case-insensitive, and words are separated by spaces.

# Examples

# "The key and the lock is there" -> ['key', 'lock']
# "The" (case-insensitive) is followed by "key" and "the" is followed by "lock" hence, the output is ['key', 'lock'].
# "The the and the The" -> ['the', 'and', 'The']
# "the" follows "The", "and" follows "the" and "The" follows "the".
            
        
