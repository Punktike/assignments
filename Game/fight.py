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
        hero["health"] -= hpnr
        hero["xp"] += xpnr
        print(f"{hero['name']} took {hpnr} damage and got {xpnr} xp")
        input("Press enter to continue")
    
    def bossfight(hero:dict, enemytype:enemy):
        enemydif = enemytype.getdifficulty()
        print(
            "You encountered a boss...\n"
            "You have to fight the boss multiple times in order to beat it"
              )
        fight.dofight(hero, enemytype)




