#game
import random
import time
import os
from utils import *
from narrative import *
from enemies import *
from fight import *
from Day import Day



# If using "Online-ide" enable this boolean
# This is because it seems like Online-ide doesnt support clear() or atleast I wasnt able to make it work
# Will just print empty lines instead of using os.system("clear")
onlineide : bool = False # Does not even matter because online-ide does not support match: case
onlineideamount = 4 # The amount of empty lines it prints

disableannoyingmessages = True # Disables some "Press enter to continue" messages
onlyaskwhenneeded = False # Disables superpotion question if you have max health, Might not work
randomnarrative = True # Gives different enemies and stories for each day. Put on false for a fixed narrative
narrativetype = 0 # The story (0 is the assignment one)

# Base stats
# Should have made this be a seperate class instead of being a dictionary
hero = { 
    "name": "Hero",
    "health": 100,
    "xp": 0,
    "inventory": {},
    "skills": [],
    "MaxHealth": 100
}
currentday = Day(0) # The start day - 1
maxdays = 100

# Just to learn what lambda does
rand = lambda x,y: random.randint(x,y) 
continuegame = lambda: input("Press enter to continue")


# Should have put this in utils
def clear(): # Hopefully this wont give any errors
    if onlineide:
        # print("\033[H\033[J", end="") # Taken from the internet (This also doesnt work on "Online-ide")
        for i in range(0,onlineideamount):
            print("\n")
        return

    if os.name == "nt": # Windows
        os.system("cls")
        return
        os.system("clear") # Hopefully works for everything else

def getrandom(type : str, *args): 
    global hero

    # I dont use *args anymore but still gonna keep these just in case
    if len(args) > 1:
        print("Too many arguments in getrandom function") # Just incase I forget about this

    if len(args) == 1:
        if isinstance(args[0],enemy):
            enemytype = args[0]
        else:
            print("Invalid argumenet passed in getrandom function")

    if type == "avoid":
        nr = rand(1,100)
        if nr <= 60:
            potion()
        else:
            print("Nothing happened")

    continuegame()
    
def superpotion():
    nr = rand(1,100)
    if nr <= 15:
        item.addtoinventory(hero, items.superpotion)

# For modifying health
def modhp(dictionary, amount : int): # Ensures health doesnt go over 100
    dictionary["health"] += amount
    if dictionary["health"] > dictionary["MaxHealth"]:
        dictionary["health"] = dictionary["MaxHealth"]

# When you find a potion
def potion():
    global hero
    goodpotion = True
    nr = rand(1,2)
    if nr == 2:
        goodpotion = False
    if getinput("Use potion (y/n): "):
        if goodpotion or items.spellbook in hero["inventory"]:
            modhp(hero, rand(10,30))
            print("That potion was good!")
            print(f"Your health is now {hero['health']}")
            return
        modhp(hero, rand(10,30) * -1)
        print("That potion wasn't good...")
        print(f"Your health is now {hero['health']}")
    

# Only for y/n questions
def getinput(text : str):
    selection = input(text)
    allowed = ["y", "n"]
    while selection.lower() not in allowed:
        selection = input(text)
    if selection.lower() == "y":
        return True
    elif selection.lower() == "n":
        return False

    
# Lets you choose if to attack or not
def options(): 
    global hero
    global currentday
    enemytype : enemy = narrative.enemy(narrativetype)
    enemyname = enemytype.getname()
    print(f"As {hero['name']} is walking, they see a {enemyname} (difficulty {enemytype.getdifficulty()}) in front of them ")
    selection = getinput("Attack " + enemyname + "? (y/n): ")
    if selection == True:
        # getrandom("fight", enemytype)
        fight.dofight(hero, enemytype)
        if items.spellbook in hero["inventory"]:
            # number = 1
            superpotion()
    elif selection == False:
        getrandom("avoid")
    # currentday.increment()
    gameloop()

# Prints stats
def pstats():
    print(f"Health: {hero['health']}")
    print(f"XP: {hero['xp']}")
    print(mstats.getstats(hero) + "\n\n")

            

def startgame():
    global hero
    global narrativetype
    hero["name"] = input("What is your hero's name? ").capitalize()
    if hero["name"] == "":
        hero["name"] = "Hero"

    if randomnarrative: narrativetype = random.randint(1,5)
    print(hero["name"]+" "+narrative.introduction(narrativetype))
    continuegame()
    gameloop()

def gameover():
    clear()
    print(narrative.gameoverr(narrativetype, hero))
    print("You died...")
    thing = input("Press enter to restart or type something to end the game")
    if thing == "":
        resetgame()
    else:
        print("Goodbye!")
        exit()
    
def wingame():
    clear()
    print(narrative.win(narrativetype))
    print("You won!")
    print("You got a total of: "+hero["xp"])
    thing = input("Press enter to restart or type something to end the game")
    if thing == "":
        resetgame()
    else:
        print("Goodbye!")
        exit()    

def resetgame():
    global currentday
    global hero
    global narrativetype
    hero["health"] = 100
    hero["xp"] = 0
    hero["inventory"] = {}
    hero["skills"] = []
    hero["MaxHealth"] = 100
    currentday.day = 0
    notifyonadd.potion = 0
    if randomnarrative: narrativetype = random.randint(1,5)

# Made this only because of the superpotion
def night():
    print("The sun sets...\nAnd you go to sleep")
    if not disableannoyingmessages: continuegame()
    morning()

def morning():
    if items.superpotion in hero["inventory"]:
        if onlyaskwhenneeded and hero["health"] >= hero["MaxHealth"]:
            return
        if getinput("Do you want to drink a superpotion? (y/n): "):
            usepotion()
    else:
        print("You wake up")
        if not disableannoyingmessages: continuegame()


def usepotion():
    global hero
    item.removefrominventory(hero, items.superpotion)
    modhp(hero, 100)

def gameloop():
    global hero
    global currentday

    night()

    if hero["health"] <= 0 or currentday.day > maxdays and hero["xp"] <= 0:
        gameover()

    if currentday.day > maxdays:
        wingame()

    currentday.increment()
    currentday.checkspecial(narrativetype, hero)

    # Another death check (incase of death in checkspecial)
    if hero["health"] <= 0 or currentday.day > maxdays and hero["xp"] <= 0:
        gameover()

    if items.spellbook in hero["inventory"] and hero["xp"] >= 100:
        clear()
        print(narrative.fireball(narrativetype, hero))
        spell.addtoinventory(hero["skills"], spells.fireball)

    clear()
    pstats()
    # print(f"Inventory: {hero['inventory']}")

    print(f"Day {currentday.day} of {maxdays}")
    options()


startgame() # This single line prevents me from importing Main in any other file and I dont know how to fix it

