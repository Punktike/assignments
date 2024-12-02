# Contains the possible items (Could be in its own file and made better)
class items:
    spellbook = "📔 Spellbook"
    superpotion = "🍼 Superpotion"

    armor = "🛡 Armor"
    hppotion = "❤️ Health Boost"
    strengthpotion = "💪 Strength Boost"

    countable = [superpotion] # Items that you can have multiple of

# Contains the possible spells (Could be in its own file)
class spells:
    fireball = "🔥 Fireball"



# Does stuff with items
class item:
    def addtoinventory(dictionary, thing : items):
        # inventory = lambda: dictionary["inventory"] # Can not use lambda for this
        if thing not in dictionary["inventory"]:
            dictionary["inventory"][thing] = 1

            if thing == items.hppotion:
                dictionary["MaxHealth"] += dictionary["MaxHealth"]
            notifyonadd.notifyitem(thing)
            return
        dictionary["inventory"][thing] +=1
        notifyonadd.notifyitem(thing)

    def removefrominventory(dictionary, thing : items):
        # inventory = lambda: dictionary["inventory"]
        dictionary["inventory"][thing] -=1
        if dictionary["inventory"][thing] == 0:
            del dictionary["inventory"][thing]


# Does stuff with spells 
class spell:
    def addtoinventory(list : list, thing : spells):
        if thing not in list:
            list.append(thing)
            notifyonadd.notifyspell(thing)
            return
        
    def removefrominventory(list : list, thing : spells): # This probably wont be used anywhere
        if thing in list:
            list.remove(thing)


# This could be made better if items and spells were in their own objects
class notifyonadd:

    potion = 0

    def notifyitem(thing: items):
        print(f"You found a {thing}") 
        if thing == items.spellbook:
            print(
                "It makes some BIG changes\n" +
                "1) It teaches how to deal with poisonous potions, so from this moment, every found potion will be healing \n" +
                "2) It reveals the arcane secrets of the dungeon, so by reaching 100 experience hero can start using a fireball spell — it makes fighting goblins much easier, so no health will be lost in a fight. "+
                "3) It gives a hint about how to recognize the superpotion — a rare mixture made by goblins that can fully restore health to 100 HP. There is only a 15% chance that it may be dropped by the goblin after the fight. You put superpotions in the backpack and every morning you decide to drink it or not."
            )
            input("Press enter to continue")
        if thing == items.superpotion and notifyonadd.potion == 0:
            print(
                "You just got your first superpotion!\n"+
                'You can now drink it in the morning and restore your health to 100 points.'
            ) 
            notifyonadd.potion = 1
        if thing == items.armor:
            print(
                "You found armor!\n" +
                "It halves all damage you take."
            )
        if thing == items.strengthpotion:
            print(
                "You found a strength potion!\n" +
                "It makes you be able to beat bosses in a single fight."
            )
        if thing == items.hppotion:
            print(
                "You found a health potion!\n" +
                "It doubles your max hp."
            )
    


    def notifyspell(thing: spells):
        print(f"You unlocked {thing}")
        input("Press enter to continue")

# return inventory and spells
class mstats:
    def getstats(dictionary : dict):
        stats = ""
        for item in dictionary["inventory"].keys():
            if item in items.countable:
                stats += f"{item}: {dictionary['inventory'][item]}\n"
            else:
                stats += f"{item}\n"
        for spell in dictionary["skills"]:
            stats += f"{spell}\n"
        return stats
    
# test = {
#     "name": "Hero",
#     "health": 100,
#     "xp": 0,
#     "inventory": {},
#     "skills": []
# }

# item.addtoinventory(test, items.spellbook)
# item.addtoinventory(test, items.superpotion)
# item.addtoinventory(test, items.superpotion)
# print(mstats.getstats(test))