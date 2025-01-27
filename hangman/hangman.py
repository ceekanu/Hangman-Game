# Python Program to illustrate
# Hangman Game
import random
from collections import Counter

themes = {
    "Holidays": [
        "christmas", "valentine's day", "easter", 
        "independence day" ,"new year's", "thanksgiving" ,"saint patrick's day"
    ],
    "Colors": [
        "purple", "orange", "black", "white", "brown", "red", "pink", "yellow",
        "blue", "green", "gold", "silver"
    ],
    "Animals": [
        "lion", "zebra", "elephant", "fish", "tiger", "panda",
    "kangaroo", "whale", "shark", "dolphin", "dog", "cat" 
    ],
    "Countries": [
    "nigeria", "united states", "united kingdom", "china",
    "australia", "india", "south africa", "greece", "ghana"
    ]
}

def choose_theme():
    #This allows the player to pick a theme to play
    print("Pick a theme")
    theme_names=list(themes.keys())
    for i, theme in enumerate(theme_names):
        print(f"{i+1}. {theme}")

    while True:
        try:
            theme_choice = int(input("Type the number of your chosen theme:"))-1
            if 0<=theme_choice<len(theme_names):
               return themes[theme_names[theme_choice]]
            else:
                print("Please choose a valid theme.")
        except ValueError:
            print("Please enter a valid integer based on your chosen theme.")

def play_game():
    print("\nWelcome to Hangman! A game that tests your ability to guess words correctly.")

    #User selects a theme
    someWords = choose_theme()
    #A word is randomly selected from the theme chosen by the user
    word = random.choice(someWords).upper()
  
    print("\nIt's time to guess the word!") 
    #Display blanks for the word to be guessed
    print("_ " * len(word))

    playing=True
    #Track the guessed letter
    letterGuessed= ''
    #Number of lives
    lives = len(word)+3
    #The flag condition for winning
    flag=0

    while lives > 0 and not flag:
        print(f"\nYou have {lives} lives remaining.")
        guess = input("\nType your letter guess: ").upper()

    #Checking the user's input
        if len(guess)>1:
            print("\nEnter just one letter!")
            continue
        elif guess in letterGuessed:
            print("\nYou already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("\nEnter a letter!")
            continue
        
        #User loses a life if a letter was guessed incorrectly
        if guess in word:
            letterGuessed.append(guess)
        else:
            lives-=1
        

        #Print the word
        correct_guess = True
        for char in word:
            if char.isalpha() and char in letterGuessed:
                print(char, end=' ')
            elif char in " '":
                print(char, end=" ") #shows existing spaces and apostrophes
            else:
                print("_", end=" ")
                correct_guess = False
            
        if correct_guess:
            print(f"\nGreat job! \nYou guessed the word: {word}")
            flag = 1
            break

    if not flag:
        print(f"\nTry again! The correct word was:{word}")
if __name__ == '__main__':
    while True:
        play_game()
        restart_game= input("\nDo you want to play again?(yes/no): ").lower().strip()
        if restart_game not in ["yes", "y"]:
            print("\nThanks for playing! See you next time!")
            break