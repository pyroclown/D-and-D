import math
import random


def genNumber():
    numbers = [random.randrange(1,6),random.randrange(1,6),random.randrange(1,6),random.randrange(1,6), random.randrange(1,6)]
    numbers.sort()
    numbers.pop(0)
    rawScore = 0
    for x in numbers:
        rawScore += x
    return rawScore

abilityScores = [genNumber(), genNumber(), genNumber(), genNumber(), genNumber(), genNumber()]
abilityScores.sort()
race = input("Race: ")
type = input("Class: ")

strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0

def addHuman():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += 1
    dexterity += 1
    constitution += 1
    intelligence += 1
    wisdom += 1
    charisma += 1
def addHillDwarf():
    global constitution
    global wisdom
    constitution += 2
    wisdom += 1
def addMountainDwarf():
    global strength
    global constitution
    constitution += 2
    strength += 2
def addHighElf():
    global dexterity
    global intelligence
    dexterity += 2
    intelligence += 1
def addWoodElf():
    global dexterity
    global wisdom
    dexterity += 2
    wisdom += 1
def addDarkElf():
    global dexterity
    global charisma
    dexterity += 2
    charisma += 1
def addLightfootHalfling():
    global dexterity
    global charisma
    dexterity += 2
    charisma += 1
def addStoutHalfling():
    global dexterity
    global constitution
    dexterity += 2
    constitution += 1
def addDragonborn():
    global strength
    global charisma
    strength += 2
    charisma += 1
def addForestGnome():
    global dexterity
    global intelligence
    intelligence += 2
    dexterity += 1
def addRockGnome():
    global constitution
    global intelligence
    intelligence += 2
    constitution += 1
def addHalfElf():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    charisma += 2
    dexterity += 1
def addHalfOrc():
    global strength
    global constitution
    strength += 2
    constitution += 1
def addTiefling():
    global intelligence
    global charisma
    charisma += 2
    intelligence += 1


raceOptions = {
    "Human" : addHuman,
    "Hill Dwarf" : addHillDwarf,
    "Mountain Dwarf" : addMountainDwarf,
    "High Elf" : addHighElf,
    "Wood Elf" : addWoodElf,
    "Dark Elf" : addDarkElf,
    "Lightfoot Halfling" : addLightfootHalfling,
    "Stout Halfling" : addStoutHalfling,
    "Dragonborn" : addDragonborn,
    "Forest Gnome" : addForestGnome,
    "Rock Gnome" : addRockGnome,
    "Half Elf" : addHalfElf,
    "Half Orc" : addHalfOrc,
    "Tiefling" : addTiefling
}
def addBarbarian():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[5]
    dexterity += abilityScores[3]
    constitution += abilityScores[4]
    intelligence += abilityScores[1]
    wisdom += abilityScores[2]
    charisma += abilityScores[0]
def addBard():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[3]
    dexterity += abilityScores[1]
    constitution += abilityScores[2]
    intelligence += abilityScores[0]
    wisdom += abilityScores[4]
    charisma += abilityScores[5]
def addCleric():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[4]
    dexterity += abilityScores[2]
    constitution += abilityScores[3]
    intelligence += abilityScores[0]
    wisdom += abilityScores[5]
    charisma += abilityScores[1]
def addDruid():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[2]
    dexterity += abilityScores[4]
    constitution += abilityScores[3]
    intelligence += abilityScores[1]
    wisdom += abilityScores[5]
    charisma += abilityScores[0]
def addFighter():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[5]
    dexterity += abilityScores[3]
    constitution += abilityScores[4]
    intelligence += abilityScores[2]
    wisdom += abilityScores[1]
    charisma += abilityScores[0]
def addMonk():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[1]
    dexterity += abilityScores[5]
    constitution += abilityScores[3]
    intelligence += abilityScores[2]
    wisdom += abilityScores[4]
    charisma += abilityScores[0]
def addPaladin():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[4]
    dexterity += abilityScores[1]
    constitution += abilityScores[3]
    intelligence += abilityScores[0]
    wisdom += abilityScores[2]
    charisma += abilityScores[5]
def addRanger():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[2]
    dexterity += abilityScores[5]
    constitution += abilityScores[4]
    intelligence += abilityScores[1]
    wisdom += abilityScores[3]
    charisma += abilityScores[0]
def addRouge():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[0]
    dexterity += abilityScores[5]
    constitution += abilityScores[4]
    intelligence += abilityScores[1]
    wisdom += abilityScores[2]
    charisma += abilityScores[3]
def addSorcerer():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[2]
    dexterity += abilityScores[4]
    constitution += abilityScores[3]
    intelligence += abilityScores[1]
    wisdom += abilityScores[5]
    charisma += abilityScores[0]
def addWarlock():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[2]
    dexterity += abilityScores[4]
    constitution += abilityScores[3]
    intelligence += abilityScores[1]
    wisdom += abilityScores[5]
    charisma += abilityScores[0]
def addWizard():
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    strength += abilityScores[1]
    dexterity += abilityScores[4]
    constitution += abilityScores[3]
    intelligence += abilityScores[5]
    wisdom += abilityScores[2]
    charisma += abilityScores[0]


classOptions = {
    "Barbarian" : addBarbarian,
    "Bard" : addBard,
    "Cleric" : addCleric,
    "Druid" : addDruid,
    "Fighter" : addFighter,
    "Monk" : addMonk,
    "Paladin" : addPaladin,
    "Ranger" : addRanger,
    "Rouge" : addRouge,
    "Sourcerer" : addSorcerer,
    "Warlock" : addWarlock,
    "Wizard" : addWizard
}
classHealth = {
    "Barbarian" : 12,
    "Bard" : 8,
    "Cleric" : 8,
    "Druid" : 8,
    "Fighter" : 10,
    "Monk" : 8,
    "Paladin" : 10,
    "Ranger" : 10,
    "Rouge" : 8,
    "Sourcerer" : 6,
    "Warlock" : 8,
    "Wizard" : 6
}
raceText = {
    "Human" : "\n-No Additional Racial Traits",
    "Hill Dwarf" : "\n-Darkvision \n-Advantage on poision rolls \n-Resistant to poision damage \n-Proficient with Battleaxe, Handaxe, Throwing Hammer, Warhammer \n-Proficient with 1 artisans tool \n-+1 to HP per level",
    "Mountain Dwarf" : "\n-Darkvision \n-Advantage on poision rolls \n-Resistant to poision damage \n-Proficient with Battleaxe, Handaxe, Throwing Hammer, Warhammer \n-Proficient with 1 artisans tool \n-Proficient with light/medium armor",
    "High Elf" : "\n-Darkvision \n-Advantage on throws against being charmed and immune to sleep \n-Meditate instead of sleeping \n-Proficient with Longsword, Shortsword, Shortbow, and Longbow \n-One Cantrip",
    "Wood Elf" : "\n-Darkvision \n-Advantage on throws against being charmed and immune to sleep \n-Meditate instead of sleeping \n-Proficient with Longsword, Shortsword, Shortbow, and Longbow \n-Can hide in light obstruction",
    "Dark Elf" : "\n-Improved Darkvision \n-Advantage on throws against being charmed and immune to sleep \n-Meditate instead of sleeping \n-Disadvantage on rolls in sunlight \n-Proficient with Rapiers, Shortswords, and Hand Crossbows",
    "Lightfoot Halfling" : "\n-May reroll a 1 and use new roll \n-Advantage against being frightened \n-Can attempt to hide even when obscured only by another creature",
    "Stout Halfling" : "\n-May reroll a 1 and use new roll \n-Advantage against being frightened \n-Advantage against poision rolls \n Resistant to poision",
    "Dragonborn" : "\n-Breath attack does 2d6 on failed save \n-Resistance to breath damage type attacks",
    "Forest Gnome" : "\n-Darkvision \n-Advantage against rolls concerning magic in any way \n-Know minor illusion cantrip \n-Can communicate with small or tiny beasts",
    "Rock Gnome" : "\n-Darkvision \n-Advantage against rolls concerning magic in any way \n-Double proficiency bonus to History checks \n-Proficient with Tinkers Tools \n-Can create Clockwork toy, Fire Starter, and Music Box. Costs 10gp and 1 hour",
    "Half Elf" : "\n-Darkvision \n-Advantage on throws against beign charmed and immune to sleep \n-Gain 2 additional skill proficiencies",
    "Half Orc" : "\n-Darkvision \n-Proficient in intimidation \n-Can choose to regain 1 HP when downed once inbetween long rests \n-Crit for 3x damage",
    "Tiefling" : "\n-Darkvision \n-Resistant to fire damage \n-Know thaumaturgy cantrip"
}
classText = {
    "Barbarian" : "Test Works",
    "Bard" : "Test Works",
    "Cleric" : "",
    "Druid" : "",
    "Fighter" : "",
    "Monk" : "",
    "Paladin" : "",
    "Ranger" : "",
    "Rouge" : "",
    "Sourcerer" : "",
    "Warlock" : "",
    "Wizard" : "",
}
baseSpeed = {
    "Human" : "30",
    "Hill Dwarf" : "25",
    "Mountain Dwarf" : "25",
    "High Elf" : "30",
    "Wood Elf" : "35",
    "Dark Elf" : "30",
    "Lightfoot Halfling" : "25",
    "Stout Halfling" : "25",
    "Dragonborn" : "30",
    "Forest Gnome" : "25",
    "Rock Gnome" : "25",
    "Half Elf" : "30",
    "Half Orc" : "30",
    "Tiefling" : "30"
}
baseLanguage = {
    "Human" : "Common, Additional language of choice",
    "Hill Dwarf" : "Common, Dwarven",
    "Mountain Dwarf" : "Common, Dwarven",
    "High Elf" : "Common, Elvish, Additional language of choice",
    "Wood Elf" : "Common, Elvish",
    "Dark Elf" : "Common, Elvish",
    "Lightfoot Halfling" : "Common, Halfling",
    "Stout Halfling" : "Common, Halfling",
    "Dragonborn" : "Common, Draconic",
    "Forest Gnome" : "Common, Gnomish",
    "Rock Gnome" : "Common, Gnomish",
    "Half Elf" : "Common, Elvish, Additional language of choice",
    "Half Orc" : "Common, Orcish",
    "Tiefling" : "Common, Infernal"
}


raceOptions[race]()
classOptions[type]()

modStrength = (strength - 10) // 2
modDexterity = (dexterity - 10) // 2
modConstitution = (constitution - 10) // 2
modIntelligence = (intelligence - 10) // 2
modWisdom = (wisdom - 10) // 2
modCharisma = (charisma - 10) // 2

health = classHealth[type] + modConstitution

raceTraits = raceText[race]
classTraits = classText[type]
raceSpeed = baseSpeed[race]
language = baseLanguage[race]

playerName = input("Player Name: ")
characterName = input("Character Name: ")
playerHeight = input("Character Height: ")
playerWeight = input("Character Weight: ")
playerGender = input("Gender: ")
playerBackground = input("Background: ")


f = open(playerName + ".txt", "w")
f.write("Player Name: " + playerName + "\n")
f.write("Character Name: " + characterName + "\n")
f.write("Race: " + race + "\n")
f.write("Class: " + type + "\n")
f.write("Gender: " + playerGender + "\n")
f.write("Background: " + playerBackground + "\n")
f.write("Height: " +  playerHeight + "\n")
f.write("Weight: " + playerWeight + "\n")
f.write("\n")
f.write("Health: " + str(health) + "\n")
f.write("Proficiency Bonus: " + "+2" + "\n")
f.write("\n")
f.write("Strength: " + str(strength) + " , " + str(modStrength) + "\n")
f.write("Dexterity: " + str(dexterity) + " , " + str(modDexterity) + "\n")
f.write("Constitution: " + str(constitution) + " , " + str(modConstitution) + "\n")
f.write("Intelligence: " + str(intelligence) + " , " + str(modIntelligence) + "\n")
f.write("Wisdom: " + str(wisdom) + " , " + str(modWisdom) + "\n")
f.write("Charisma: " + str(charisma) + " , " + str(modCharisma) + "\n")
f.write("\n")
f.write("Racial Traits: " + str(raceTraits) + "\n")
f.write("\n")
f.write("Class Traits: " + str(classTraits) + "\n")
f.write("\n")
f.write("Base Speed: " + str(raceSpeed) + "\n")
f.write("Languages: " + str(language) + "\n")
f.write("\n")
f.close()
