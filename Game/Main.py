#game
import random
import time
import os
from utils import *
from narrative import *
from enemies import *
from fight import *

# If using "Online-ide" enable this boolean
# This is because it seems like Online-ide doesnt support clear() or atleast I wasnt able to make it work
# Will just print empty lines instead of using os.system("clear")
onlineide : bool = False
onlineideamount = 4 # The amount of empty lines it prints

disableannoyingmessages = True # Disables some "Press enter to continue" messages
onlyaskwhenneeded = False # Disables superpotion question if you have 100  health
randomnarrative = True # Gives different enemies and stories for each day. Put on false for a fixed narrative
narrativetype = 0 # The story (0 is the assingement one)

# Base stats
hero = {
    "name": "Hero",
    "health": 100,
    "xp": 0,
    "inventory": {},
    "skills": []
}
currentday = 1
maxdays = 100



# Just to learn what lambda does
rand = lambda x,y: random.randint(x,y) 
continuegame = lambda: input("Press enter to continue")


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


number = 0 # Used to prevent recursion from doing continue message 2 times 
def getrandom(type : str, *args): # I could split this up into multiple functions and it would be way easier to use..... 
    global hero
    global number

    if len(args) > 1:
        print("Too many arguments in getrandom function") # Just incase I forget about this

    if len(args) == 1:
        if isinstance(args[0],enemy):
            enemytype = args[0]
        else:
            print("Invalid argumenet passed in getrandom function")


    # if type == "fight": # Should maybe make this be in a seperate class
    #     enemydifficulty = enemytype.getdifficulty()
    #     hpnr = rand(10,30) * enemydifficulty
    #     xpnr = rand(10,25) * enemydifficulty
    #     if spells.fireball in hero["skills"]:
    #         hpnr = 0
    #     hero["health"] -= hpnr
    #     hero["xp"] += xpnr
    #     print(f"{hero['name']} took {hpnr} damage and got {xpnr} xp")
    #     if items.spellbook in hero["inventory"]:
    #         number = 1
    #         getrandom("superpotion")

    if type == "avoid":
        nr = rand(1,100)
        if nr <= 60:
            #do something
            potion()
        else:
            print("Nothing happened")
    
    # if type == "superpotion":
    #     nr = rand(1,100)
    #     if nr <= 15:
    #         item.addtoinventory(hero, items.superpotion)
    # if number == 0:
    #     continuegame()

    match number:
        case 0:
            continuegame()
        # case 1:
        #     number = 0
    
def superpotion():
    nr = rand(1,100)
    if nr <= 15:
        item.addtoinventory(hero, items.superpotion)

def modhp(dictionary, amount : int): # Ensures health doesnt go over 100
    dictionary["health"] += amount
    if dictionary["health"] > 100:
        dictionary["health"] = 100

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

    

def options(): 
    global hero
    global currentday
    enemytype : enemy = narrative.enemy(narrativetype)
    enemyname = enemytype.getname()
    print(f"As you are walking, you see a {enemyname} (difficulty {enemytype.getdifficulty()}) in front of you ")
    selection = getinput("Attack " + enemyname + "? (y/n): ")
    if selection == True:
        # getrandom("fight", enemytype)
        fight.dofight(hero, enemytype)
        if items.spellbook in hero["inventory"]:
            # number = 1
            superpotion()
    elif selection == False:
        getrandom("avoid")
    currentday+=1
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
    currentday = 1
    notifyonadd.potion = 0
    if randomnarrative: narrativetype = random.randint(1,5)

# Made this only because of the superpotion
def night():
    print("The sun sets...\nAnd you go to sleep")
    if not disableannoyingmessages: continuegame()
    morning()

def morning():
    if items.superpotion in hero["inventory"]:
        if onlyaskwhenneeded and hero["health"] >= 100:
            return
        if getinput("Do you want to drink a superpotion? (y/n): "):
            usepotion()
    else:
        print("You wake up")
        if not disableannoyingmessages: continuegame()


def usepotion():
    global hero
    item.removefrominventory(hero, items.superpotion)
    hero["health"] = 100

def gameloop():
    global hero
    global currentday

    night()

    if hero["health"] <= 0 or currentday > maxdays and hero["xp"] <= 0:
        gameover()

    if currentday > maxdays:
        wingame()

    if currentday == 5:
        clear()
        print(narrative.spellbook(narrativetype, hero))
        item.addtoinventory(hero, items.spellbook)

    if currentday == 10:
        clear()
        print(f"You beat day 10 with {hero['xp']} xp")
        continuegame()

    if currentday % 20:
        fight.bossfight

    if items.spellbook in hero["inventory"] and hero["xp"] >= 100:
        clear()
        print(narrative.fireball(narrativetype, hero))
        spell.addtoinventory(hero["skills"], spells.fireball)

    clear()
    pstats()
    # print(f"Inventory: {hero['inventory']}")

    print(f"Day {currentday} of {maxdays}")
    options()

startgame()
