import random
from utils import *
from enemies import *

class fight:

    def dofight(hero:dict, enemytype:enemy): 
        enemydifficulty = enemytype.getdifficulty()
        hpnr = random.randint(10,30) * enemydifficulty
        xpnr = random.randint(10,25) * enemydifficulty
        if spells.fireball in hero["skills"] and enemydifficulty < 2:
            hpnr = 0
        elif spells.fireball in hero["skills"] and enemydifficulty >= 2:
            hpnr = hpnr / 1.75
            if items.armor in hero['inventory']:
                hpnr = hpnr / 2

        # To prevent one shots
        if hpnr >= 100 and hero['MaxHealth'] < 150:
            hpnr = 99

        hero["health"] -= hpnr
        hero["xp"] += xpnr
        print(f"{hero['name']} took {hpnr} damage and got {xpnr} xp")
        input("Press enter to continue")
    
    def bossfight(hero:dict, enemytype:enemy): # TODO: cant use superpotions in this rn, making this impossible
        print(
            "You encountered a boss...\n"
            "You have to fight the boss 3 times in order to beat it"
              )
        
        # This could probably be done better
        fight.dofight(hero, enemytype)
        if hero["health"] <= 0:
            return
        if items.strengthpotion in hero["inventory"]:
            print("You won the fight and beat the boss")
            return
        fight.dofight(hero, enemytype)
        if hero["health"] <= 0:
            return
        fight.dofight(hero, enemytype)
        if hero["health"] <= 0:
            return
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
        item.addtoinventory(random.choice([items.strengthpotion, items.armor, items.hppotion]))



