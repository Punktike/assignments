# Narrative stuff
import random
from enemies import enemies

class narrative:

    def introduction(int):
        match int:
            case 0:
                return "is a knight walking to a city but along the way they encounter some goblins..."
            case 1:
                return "is a barbarian hunter, who is searching for a legendary treasure..."
            case 2:
                return "is a detective investigating a murder..."
            case 3:
                return "is a guard defending a forest from sorcerers"
            case 4:
                return "is a cleric trying to find out the cause of a dangerous disease..."
            case 5:
                return "is a character in a fairytale"
    
    def enemy(int):
        match int:

            case 0:
                return enemies.goblin

            case 1:
                return random.choice([
                    enemies.goblin,
                    enemies.orc,
                    enemies.troll,
                    enemies.dragon,
                    enemies.goblinking
                    ]) 
            case 2:
                return random.choice([
                    enemies.vampire,
                    enemies.zombie,
                    enemies.skeleton,
                    enemies.werewolf,
                    enemies.vampireking
                ])
            case 3:
                return random.choice([
                    enemies.ghost,
                    enemies.forestguardian,
                    enemies.windspirit,
                    enemies.stonegiant,
                    enemies.darksorcerer
                ])
            case 4:
                return random.choice([
                    enemies.darkelf,
                    enemies.darkpaladin,
                    enemies.darkwizard,
                    enemies.darkarcher,
                    enemies.darkwyrm
                ])
            case 5:
                return random.choice([
                    enemies.djinn,
                    enemies.treant,
                    enemies.wendigo,
                    enemies.banshee,
                    enemies.naga
                ])
    
    def boss(int):
        match int:
            case 1:
                return enemies.phoenix
            case 2:
                return enemies.mutantbeast
            case 3:
                return enemies.darknecromancer
            case 4:
                return enemies.hydra
            case 5:
                return enemies.kraken
            
    def spellbook(int, hero : dict):
        match int:
            case 0:
                return f"While walking, {hero['name']} found a spellbook resting on a rock."
            case 1:
                return f"After defeating an enemy, {hero['name']} found a spellbook."
            case 2:
                return f"While trying to find clues, {hero['name']} found a spellbook."
            case 3:
                return f"While on patrol, {hero['name']} found a spellbook."
            case 4:
                return f"After trying to find a cure, {hero['name']} found a spellbook."
            case 5:
                return f"A spellbook fell on the ground out of nowhere and {hero['name']} picked it up."
        
    def fireball(int, hero : dict):
        match int:
            case 0:
                return f"After winning a fight against a goblin, {hero['name']} suddenly learnt how to use magic"
            case 1:
                return f"Although {hero['name']} prefers using fists, they havee also picked up some magic"
            case 2:
                return f"While investigating a scroll, {hero['name']} found instructions on how to use magic"
            case 3:
                return f"After defeating a sorcerer, {hero['name']} found instructions on how to use a fireball"
            case 4:
                return f"A friendly wizard told {hero['name']} how to use a fireball"
            case 5:
                return f"{hero['name']} suddenly knows how to use a fireball"
            
    def gameoverr(int, hero:dict):
        match int:
            case 0:
                return f"{hero['name']} never managed to make it to the city..."
            case 1:
                return f"{hero['name']} was defeated after a fierce battle..."
            case 2:
                return f"{hero['name']} was never able to solve the murder..."
            case 3:
                return "The forest fell into the hands of the sorcerers..."
            case 4:
                return "The disease turned into a pandemic..."
            case 5:
                return "The fairytale had a bad ending..."
            
    def win(int):
        match int:
            case 0:
                return "made it to the city!"
            case 1:
                return "found the treasure"
            case 2:
                return "solved the murder"
            case 3:
                return "was able to defend the forest"
            case 4:
                return "was able to succesfully make a cure"
            case 5:
                return "finished the fairytale"