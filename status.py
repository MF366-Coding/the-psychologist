
# The Status Module

from clsCmd import clear

class Status:
    class Names:
        class Player:
            name = "Peter"
            surname = "Nest"
            full = name+" "+surname

        class Mother:
            name = "Linda"
            surname = "Johnson"
            full = name+" "+surname
            
        class StepFather:
            name = "Gary"
            surname = "Johnson"
            full = name+" "+surname

        class Father:
            name = "Joseph"
            surname = "Nest"
            full = name+" "+surname
            
        class Psychologist:
            name = "Mary"
            surname = "Nice"
            full = name+" "+surname
    
    class Health:
        meter = 150
        lifeString = str(maxim)
        full = str("Health: "+lifeString+" HP\n")
        
    class Rage:
        meter = False
        full = str("In rage? "+meter+"\n")
        
    class Hunger:
        meter = False
        full = str("Hungry? "+meter+'\n')
        
    # Still gonna add much more :D
        
def statusEdit(amount, change):
    if change == 1:
        if amount == 0:
            pass
    
