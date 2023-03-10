
# At home

import chapter2
import phase2
import gameOver
import wrongInput
import status
from clsCmd import clear

class Enemies:
    class Bully:
        strikes = 6
        knife = False
        hp_deal = 15
    
    class Teacher:
        strikes = 2
        knife = True
        knifeStrikes = 1
        hp_deal = 5
    
    class Principal:
        strikes = 4
        knife = False
        hp_deal = 10

def run():
    clear()
    input("Chapter 1 | 'A Not That Regular Day at School' | By: MF366")
    clear()
    input("[MUM] Peter! Wake up, Peter!")
    clear()
    ask = input("Wake up?\n\t[Y]es\n\t[N]o\n\nType cmd: ")

    if ask == 'y' or ask == 'Y':
        clear()
        input("You woke up.\nYou're heading to the kitchen.\nYou see your stepfather.")
        clear()
        ask = input("[S]ay 'Hi!' to stepfather\n[I]gnore him\n\nType cmd: ")
        if ask == 's' or ask == 'S':
            clear()
            input("[STEPFATHER] Helloooo, idiot!\n[...] It's better when you're crying in your bed LMAO!")
            clear()
            input("Hit ENTER to continue...")
            clear()
            phase2.nothing()
            
        elif ask == 'i' or ask == 'I':
            clear()
            input("[STEPFATHER] Did you just ignore me? SHOW SOME RESPECT, YOU LITTLE PIECE OF...")
            clear()
            input("[STEPFATHER] When I put my hands on you next time, I'll make sure you'll learn your lesson, idiot!")
            clear()
            input("Hit ENTER to continue...")
            clear()
            phase2.nothing()
            
        else:
            wrongInput.run()
            
    elif ask == 'n' or ask == 'N':
        clear()
        input("Your mother forced you to wake up.\nShe told you to go to the kitchen.\nYou see your stepfather.")
        clear()
        ask = input("[S]ay 'Hi!' to stepfather\n[I]gnore him\n\nType cmd: ")

    else:
        wrongInput.run()
        