
# The Psychologist
# By MF366 and Norb
# If you use this project, please identify us as the main project's creators.
# Repo available at: https://github.com/MF366-Coding

# To play, type the command that replies to the question or obaervation. 

# WARNING!
# This game may contain disturbing stuff happening.

# This project does not work without the other Chapter Files. 

# Thanks for downloading this project.

from clsCmd import clear
import wrongInput
import gameOver
import status
from chapter1 import phase1

def skip():
    clear()
    phase1.run()

def watchIntro():
    clear()
    input("Hit ENTER to continue every time you finish reading a sentence.")
    clear()
    input("In a small village, there was a boy.")
    clear()
    input("His name was "+status.Status.Names.Player.name+".\n"+status.Status.Names.Player.full)
    clear()
    input("He lost his father when he was 2.")
    clear()
    input("What the heck am I doing?")
    clear()
    input("Talking about him while talking to him...")
    clear()
    input("Yes, Peter! I am your new Psychologist!")
    clear()
    input("And I think we'll do great in our sessions! Or else...")
    clear()
    askForContinue = input("Click ENTER to continue to chapter 1 or type 'quit' to quit the game.")
    if askForContinue == 'quit':
        clear()
        print("\nApp quitted by player's wish.\n")
        quit()
    else:
        phase1.run()

if __name__ == '__main__':
    clear()
    askForSkip = str(input("Skip intro?\n\t[Y]es\n\t[N]o\n\nType cmd: "))

    if askForSkip == 'y' or askForSkip == 'Y':
        skip()
    elif askForSkip == 'n' or askForSkip == 'N':
        watchIntro()
    else:
        wrongInput.run()
