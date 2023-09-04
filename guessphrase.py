from random import choice
import os
import time

def cls(seconds=1):
    time.sleep(seconds)
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For other operating systems (Unix/Linux)

# Intro Screen to show how game works
cls(0)
print("**************************************************************************")
print("*   Welcome to ===>>> GUESS THE PHRASE! <<<===\n")
print("*   By Samir Tambe | License: MIT License\n")
print("*   INSTRUCTIONS:")
print("*   A blanked out phrase will appear like so:\n")
print("*   ---- - -- ----- ------- -- --- ----- -------- ------\n")
print("*   > Enter ONE LETTER, Press Enter or Return")
print("*   > If letter is in phrase, all occurences will appear | increase score")
print("*   > If letter is not in phrase | decrease score ")
print("*   > If you guess a vowel in the phrase, then no change in score")
print("*   > NOTE: There is no puncuation in the phrase")
print("*   > Guess all letters to win the game ")
print("*   > Enter . to quit the game at any time")
print("**************************************************************************")
input("Press any key to continue.")

phraseList = list()
fileHandle = open('phrases.txt')

# Load phrases from a file and randomly select one
for line in fileHandle:
    phraseList.append(line.strip())
phrase = choice(phraseList)

correctGuesses = set() #initialize empty string to store letters guessed correcty by user
wrongGuesses = set()
# numberGuesses is a tuple as the number chars will never change
numberGuesses = ('0','1','2','3','4','5','6','7','8','9')
# consonants is a tuple as the number chars will never change
consonants = ('B','C','D','F','G','H','J',
                'K','L','M','N','P','Q','R',
                'S','T','V','W','X','Y','Z')
complete = False
firstIteration = True
letterOfPhrase = []
score = 1

while complete == False:
    if firstIteration == False:
        cls(0)
        letterOfPhrase = [letter if letter in correctGuesses else '-' for letter in phrase]
        print("Score : ", score, "\n")
        print("".join(letterOfPhrase))
        print()
        ui = input('Enter a letter : ')
    # for the first iteration force enter SPACE so
    # displayed blank phrase will have spaces in it
    else: 
        ui = ' '
        firstIteration = False
    # if user enters '.' then game ends
    if ui == '.':
        quit()
    # if user enters input that is more than ONE character or a number then 
    elif len(ui) > 1 or ui in numberGuesses:
        print('Invalid Input. Only ONE letter allowed. No change in score')
        time.sleep(2)
        continue

    ui = ui.upper()
    
    if ui in wrongGuesses or ui in correctGuesses:
        print(ui,"was already guessed - no change in score.")
        time.sleep(2)
    elif ui in phrase:
        correctGuesses.add(ui)
        letterOfPhrase = [letter if letter in correctGuesses else '-' for letter in phrase]
        if ui in consonants:
            score += 1
        if "".join(letterOfPhrase) == phrase:
            complete = True
            print('You win! you correctly guessed : ',phrase)
            print('Your score is : ', score)
            quit()
    else:
        wrongGuesses.add(ui)
        score -= 1
        print(ui,'is not in phrase.')
        if score < 0:
            print("You guessed incorrectly too many times and your score is below ZERO. Game Over.")
        time.sleep(1)