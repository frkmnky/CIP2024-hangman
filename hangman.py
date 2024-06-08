import random
import time
import os

#function that prints the answer with letters hidden
def print_word_hidden(answer_letters):
    answer_hidden = []
    for i in range(len(answer_letters)):
        answer_hidden.append("*")
    return answer_hidden

#set max number of guesses for the game
GUESSES = 7

#ASCII art for hangman
hangman = ['''
      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |      | |
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |      | 
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |       
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |     --|
     |       |
     |       
     |
    _|___
    ''', '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
    _|___
    ''','''
      _______
     |/      |
     |      (_)
     |       
     |       
     |       
     |
    _|___
    ''','''
      _______
     |/      |
     |      
     |       
     |       
     |       
     |
    _|___
    ''']

#get word list from text document and assign to list variable
word_list = open("secondgradewordlist.txt", "r").read().split()

#create empty list for letters of the word
answer_letters = []
answer_hidden = []

#get a random word from the list and break it down into letters
answer = random.choice(word_list)
for i in range(len(answer)):
    answer_letters.append(answer[i])

#helper function to draw hidden word
answer_hidden = print_word_hidden(answer_letters)

#introduction to the game and how to play
print("_______________________________________________________________________________________________")
print('''
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba, 
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a 
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88 
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88 
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88 
                                    aa,    ,88                                
                                     "Y8bbdP"                                 

      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |      | |
     |
    _|___
''')
print("__________________________________________________________________________________________________________")
time.sleep(1)
print("Welcome to Hangman: Second Grade Edition!\n")
print("Can you guess the word? You have", GUESSES, "chances!")
print("Hint: The word is", len(answer), "letters long.")

#Start the game!
for i in range(GUESSES):
    print()
    print(hangman[GUESSES - 1])
    print(answer_hidden)
    #ask for user guess and make sure it is lower case
    letter_guess = input("Guess a letter: ")
    letter_guess = letter_guess.lower()
    time.sleep(0.5)

    #check if the letter guessed is in the word
    if letter_guess in answer_letters:
        print("Good guess! The letter", letter_guess, "is in the word!")
        time.sleep(0.5)
        #this loop replaces the hidden word placeholder with the letter if correctly guessed
        for i in range(len(answer_letters)):
            if letter_guess == answer_letters[i]:
                answer_hidden[i] = letter_guess
    else:
        print("\nThat letter is not a part of the word.")
        GUESSES -= 1
        print("You have", GUESSES, "chances left.")
        time.sleep(0.5)

    #clear screen
    os.system('cls')

    #win state check
    if answer_hidden == answer_letters:
        print("\n______________________________________________________________")
        print('Congrats! You guessed the word! The word was "' + answer + '".')
        break

    #loss state check
    if GUESSES == 0:
        print("\n______________________________________________________________")
        print('You have run out of guesses. The word was "' + answer + '".')
        break
