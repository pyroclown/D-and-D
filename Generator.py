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
    # to do add random
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
    "Human" : "T",
    "Hill Dwarf" : "",
    "Mountain Dwarf" : "",
    "High Elf" : "",
    "Wood Elf" : "",
    "Dark Elf" : "",
    "Lightfoot Halfling" : "",
    "Stout Halfling" : "",
    "Dragonborn" : "",
    "Forest Gnome" : "",
    "Rock Gnome" : "",
    "Half Elf" : "",
    "Half Orc" : "",
    "Tiefling" : ""
}
classText = {
    "Barbarian" : "T",
    "Bard" : "",
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

playerName = input("Player Name: ")
playerHeight = input("Character Height: ")
playerWeight = input("Character Weight: ")
playerGender = input("Gender: ")
playerBackground = input("Background: ")


f = open(playerName + ".txt", "w")
f.write("Player Name: " + playerName + "\n")
f.write("Gender: " + playerGender + "\n")
f.write("Race: " + race + "\n")
f.write("Class: " + type + "\n")
f.write("\n")
f.write("Racial Traits: " + str(raceTraits) + "\n")
f.write("Class Traits: " + str(classTraits) + "\n")
f.write("\n")
f.write("Background: " + playerBackground + "\n")
f.write("Height: " +  playerHeight + "\n")
f.write("Weight: " + playerWeight + "\n")
f.write("\n")
f.write("Strength: " + str(strength) + " " + str(modStrength) + "\n")
f.write("Dexterity: " + str(dexterity) + " " + str(modDexterity) + "\n")
f.write("Constitution: " + str(constitution) + " " + str(modConstitution) + "\n")
f.write("Intelligence: " + str(intelligence) + " " + str(modIntelligence) + "\n")
f.write("Wisdom: " + str(wisdom) + " " + str(modWisdom) + "\n")
f.write("Charisma: " + str(charisma) + " " + str(modCharisma) + "\n")
f.write("\n")
f.write("Health: " + str(health) + "\n")
f.close()
