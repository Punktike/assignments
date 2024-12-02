


class enemy():

    def __init__(self, name:str, difficulty:int): # Initializes the enemy
    
        self.stats = {                            # The stats of the enemy in this instance
            "Enemyname": name,
            "Difficulty": difficulty
        }

    def getname(self):
        return self.stats["Enemyname"]
    
    def getdifficulty(self):
        return self.stats["Difficulty"]
    

# The possible enemies along with their difficulty
class enemies:

# 1
    goblin = enemy("Goblin", 1)
    orc = enemy("Orc", 1.2)
    troll = enemy("Troll", 1.5)
    dragon = enemy("Dragon", 2)
    goblinking = enemy("Goblin King", 3)

# 2
    vampire = enemy("Vampire", 1)
    zombie = enemy("Zombie", 1.2)
    skeleton = enemy("Skeleton", 1.5)
    werewolf = enemy("Werewolf", 2)
    vampireking = enemy("Vampireking", 3)

# 3 
    ghost = enemy("Ghost", 1)
    forestguardian = enemy("Forest Guardian", 1.2)
    windspirit = enemy("Wind Spirit", 1.5)
    stonegiant = enemy("Stone Giant", 2)
    darksorcerer = enemy("Dark Sorcerer", 3)

# 4
    darkelf = enemy("Dark Elf", 1)
    darkpaladin = enemy("Dark Paladin", 1.2)
    darkwizard = enemy("Dark Wizard", 1.5)
    darkarcher = enemy("Dark Archer", 2)
    darkwyrm = enemy("Dark Wyrm", 3) # Wyrm is a dragonlike creature

# 5
    djinn = enemy("Djinn", 1) #
    treant = enemy("Treant", 1.2) # Treant is a tree-like creature
    wendigo = enemy("Wendigo", 1.5)
    banshee = enemy("Banshee", 2)
    naga = enemy("Naga", 3)

# 6 Bosses
    phoenix = enemy("Phoenix", 5)
    mutantbeast = enemy("Mutant Beast", 5)
    darknecromancer = enemy("Dark Necromancer", 5)
    hydra = enemy("Hydra", 5)
    kraken = enemy("Kraken", 5)


# print(enemies.goblin.getname())
# print(enemies.goblin.getdifficulty())