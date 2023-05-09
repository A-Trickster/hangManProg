# filename = "s_sequence_3.txt"

# def openFile(filename):
#     with open(filename, "r") as file:
#         text = file.read()

#     return text

# words = openFile(filename)
import random

words= ["apple","toast","Beat","Beautiful","Bed","Belated","Believe","Below","Best","Better","Billion","Blood","Bloom","Book"]

def choseWord(words):
    return random.choice(words)

def game(word):
    # number of tries given to the player
    turns= len(word)+3
    print(turns)
    print(word)
    return 0

# test whole game
game(choseWord(words))