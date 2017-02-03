import random
word = "Hello"
# word[3] == "o"
# print(word[3])
# word[4] == "v"
# print(word[4])
# print(word)
def scramble_word(word):
    word = word[0:5]
    x = word[1:-1]
    x = list(x)
    print(x)
    random.shuffle(x)
    print(x)
    x = str(x)
    word = x + word[0:5]
    print(word)
   
scramble_word(word)
    
    
    
 