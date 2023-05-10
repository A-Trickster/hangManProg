# filename = "s_sequence_3.txt"

# def openFile(filename):
#     with open(filename, "r") as file:
#         text = file.read()

#     return text

# words = openFile(filename)
import random

words= ["apple","toast","Beat","Beautiful","Bed","Belated","Believe","Below","Best","Better","Billion","Blood","Bloom","Book"]

def choseWord(words):
    return random.choice(words).upper()

def game(word):
    # number of tries given to the player
    turns= len(word)+3
    print(turns)
    print(word)

    Input=''
    while turns>0:
        answer =""
        for letter in word:
            if letter in Input:
                answer += letter
            else:
                answer +="_"
        print(answer)
        print(Input)

        #Ask the player for input
        guess = input("Guess a letter: ").upper()
        print(guess)
    

# test whole game
game(choseWord(words))