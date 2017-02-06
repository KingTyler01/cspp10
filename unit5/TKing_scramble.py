import random
word = "Hello"
word2 = "there"
word3 = "mister"
# word[3] == "o"
# print(word[3])
# word[4] == "v"
# print(word[4])
# print(word)
def scramble_word(word):
    Inside_lets = word[1:-1]
    Inside_lets = list(Inside_lets)
    random.shuffle(Inside_lets)
    Combination = [word[0]] + Inside_lets + [word[-1]]
    word = "".join(Combination)
    return(word)
   
def scramble_phase(word,word2,word3):
    word = scramble_word(word) 
    word2 = scramble_word(word2)
    word3 = scramble_word(word3)
    scramble_phrase = word + " " + word2 + " " + word3
    print (scramble_phrase)
scramble_phase(word,word2,word3)
    
    
    