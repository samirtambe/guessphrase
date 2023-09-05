# GUESSPHRASE

## Overview
A command prompt game where a user attempts to guess all characters of a phrase that is hidden  The user guesses characters of the phrase individually.  The phrase is randomly selected from a text file.

By Samir Tambe

License: MIT License

## How to Run
### On Windows
In the command prompt, type `py guessphrase.py` OR `python guessphrase.py` and press ENTER

### Mac OS X or linux
In the terminal window type `python guessphrase.py` OR `python3 guessphrase.py` and press RETURN or ENTER.

There is also the option to run this script as an executable where you can change the permissions of the the
`guessphrase.py` file.

## How to play
A blanked out phrase will appear like:
`---- - -- ----- ------- -- --- ----- -------- ------`

- Enter ONE LETTER at a time, then Press Enter or Return
- If letter is in phrase, all occurences will appear, your score increases by 1 point
- If letter is not in phrase, your score decreases by 1 point
- If you guess a vowel in the phrase, then no change in score
- You begin with score = 1; this ensures a maximum of two incorrect guesses for the game to end
- Do not guess spaces as that is already indicated
- IMPORTANT NOTE: There is no puncuation marks in any displayed phrase
- Guess all letters to win the game
- If your score drops below zero the game will exit
- Enter `.` to quit the game
- Enter `?` for a help screen
