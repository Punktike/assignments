import random
from utils import *
from enemies import *
import os

class fight:

   

    def dofight(hero:dict, enemytype:enemy): 
        enemydifficulty = enemytype.getdifficulty()
        hpnr = random.randint(10,30) * enemydifficulty
        xpnr = random.randint(10,25) * enemydifficulty
        if spells.fireball in hero["skills"] and enemydifficulty < 2:
            hpnr = 0

        # Divides the damage if hero has fireball spell or/ and armor
        elif spells.fireball in hero["skills"] and enemydifficulty >= 2:
            hpnr = hpnr / 1.75
            if items.armor in hero['inventory']:
                hpnr = hpnr / 2

        # To prevent one shots
        if hpnr >= 100 and hero['MaxHealth'] < 150:
            hpnr = 99

        # Round the numbers to prevent them from having too many decimal places

        hpnr = round(hpnr, 0)
        xpnr = round(xpnr, 0)

        hero["health"] -= hpnr
        hero["xp"] += xpnr
        print(f"{hero['name']} took {hpnr} damage and got {xpnr} xp")
        input("Press enter to continue")
    
    def bossfight(hero:dict, enemytype:enemy): 
        if items.strengthpotion not in hero["inventory"]: 
            print(
            "You encountered a boss...\n"
            "You have to fight the boss 3 times in order to beat it"
              )
        else:
            print(
            "You encountered a boss...\n"
              )
        input("Press enter to continue")
 
        inbetween(hero, enemytype)
        fight.dofight(hero, enemytype)
        if hero["health"] <= 0:
            return
        
        inbetween(hero, enemytype)
        
        if items.strengthpotion in hero["inventory"]:
            print("You won the fight and beat the boss")
            return
        fight.dofight(hero, enemytype)
        if hero["health"] <= 0:
            return
        
        inbetween(hero, enemytype)

        fight.dofight(hero, enemytype)
        if hero["health"] <= 0:
            return
        
        inbetween(hero, enemytype)

        print("You won the fight and beat the boss")
        fight.bossdrop(hero)
    
    def bossdrop(hero:dict):
        possible = [items.strengthpotion, items.armor, items.hppotion]
        if items.strengthpotion in hero["inventory"]:
            possible.remove(items.strengthpotion)
        if items.armor in hero["inventory"]:
            possible.remove(items.armor)
        if items.hppotion in hero["inventory"]:
            possible.remove(items.hppotion)
        if len(possible) == 0:
            print("The boss dropped nothing")
        item.addtoinventory(hero, random.choice([items.strengthpotion, items.armor, items.hppotion]))

def inbetween(hero:dict, enemytype:enemy):
    clear()
    pstats(hero)
    print("Fightning " + enemytype.getname())

    if items.superpotion in hero["inventory"]:
            if getinput("Do you want to drink a superpotion? (y/n): "):
                usepotion(hero)
                clear()
                pstats(hero)


#duplicates from Main, because of a bug which prevents me from importing Main
def getinput(text : str):
    selection = input(text)
    allowed = ["y", "n"]
    while selection.lower() not in allowed:
        selection = input(text)
    if selection.lower() == "y":
        return True
    elif selection.lower() == "n":
        return False
    
def usepotion(hero : dict):
        item.removefrominventory(hero, items.superpotion)
        modhp(hero, 100)

def modhp(dictionary, amount : int): # Ensures health doesnt go over limit
    dictionary["health"] += amount
    if dictionary["health"] > dictionary["MaxHealth"]:
        dictionary["health"] = dictionary["MaxHealth"]

def clear(): # cant import the one from Main cause of a bug

    if os.name == "nt": # Windows
        os.system("cls")
        return
        os.system("clear") # Hopefully works for everything else

def pstats(hero:dict):
    print(f"Health: {hero['health']}")
    print(f"XP: {hero['xp']}")
    print(mstats.getstats(hero) + "\n\n")