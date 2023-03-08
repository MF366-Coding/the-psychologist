
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
        lifeString = str(meter)
        full = str("Health: "+lifeString+" HP\n")
        
    class Rage:
        meter = False
        full = str("In rage? "+meter+"\n")
        
    class Hunger:
        meter = False
        full = str("Hungry? "+meter+'\n')
        
    # Not sure if we are gonna add new stuff :D
        
def statusEdit(amount, change):
    if change == 1:
        if amount == 0:
            Status.Rage.meter = False
        else:
            Status.Rage.meter = True
    elif change == 2:
        Status.Health.meter += amount
    elif change == 3:
        if amount == 0:
            Status.Hunger.meter = False
        else:
            Status.Hunger.meter = True
        