from narrative import *
from utils import *
from fight import *
import os

class Day:
    def __init__(self, day : int):
        self.day = day
    
    def increment(self):
        self.day += 1

    #Probably wont need this
    def decrement(self):
        self.day -= 1

    # Checks if the day has a special event
    def checkspecial(self, narrativetype, hero):
        print("importing day")
        match self.day:
            case 5: # gives you the spellbook
                clear()
                print(narrative.spellbook(narrativetype, hero))
                item.addtoinventory(hero, items.spellbook)

            case 10: # tells you how much xp you made by this day
                clear()
                print(f"You beat day 10 with {hero['xp']} xp")
                input("Press enter to continue")

            case _:
                if self.day % 20 == 0: # gives you a boss
                    clear()
                    opponent : enemy = narrative.boss(narrativetype)
                    print(f"You get ambushed by {opponent.getname()} (Boss, difficulty {opponent.getdifficulty()})" )

                    fight.bossfight(hero, opponent)

def clear(): # cant import the one from Main cause of a bug

    if os.name == "nt": # Windows
        os.system("cls")
        return
        os.system("clear") # Hopefully works for everything else

