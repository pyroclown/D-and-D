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
    constitution += 1
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
    "Sorcerer" : addSorcerer,
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
    "Sorcerer" : 6,
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
    "Barbarian" : "\n-Rage: may rage 2 times inbetween rests. Rage adds 2 damage to melee attacks. \n-Gain resistance to Bludgeoning, Piercing, and Slashing  \n-Add constitution to AC when wearing no armor",
    "Bard" : "\n-May grant a creature 1d6 to use on any roll using a d20 \n   Must be used within 10 min \n   Can be used a number of times equal to Charisma modifier.",
    "Cleric" : "\n-Select Divine Domain, pg. 59",
    "Druid" : "\n-Gain Druidic as a language",
    "Fighter" : "\n-Fighting style: \n   Archery: +2 ranged attack rolls \n   Defense: +1 AC \n   Dueling: +2 damage when using 1 weapon \n   Great Weapon Fighting: Reroll dice showing 1 or 2 for damage with 2 handed weapons. \n-Can regen 1d10+level health inbetween rests",
    "Monk" : "\n-Add wisdom modifier to AC when wearing no armor \n-Use Dexterity for unarmed attack rolls \n-Roll d4 for unarmed damage \n-May make additional unarmed attack as a bonus action",
    "Paladin" : "\n-Can detect evil and good, can use 1 + Charisma modifier times inbetween long rests \n-Can heal creatures for 5 x level HP ",
    "Ranger" : "\n-Choose monster type as favored enemy \n   Advantage on tracking checks against favored enemy \n   Can speak one language spoken by favored enemy \n-Select favored terrain \n   Unable to become lost or slowed \n   Always alert to danger \n   Learn all details of creature while tracking",
    "Rouge" : "\n-Add 1d6 to damage when you have advantage or targtet is engaged in melee combat \n-Theives cant, aware of hidden signs from other rouges",
    "Sorcerer" : "\n-Select Sourcerers Origin, pg. 101",
    "Warlock" : "\n-No Additional Class Traits",
    "Wizard" : "\n-May regain 10 x level mana inbetween long rests"
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
baseGold = {
    "Barbarian" : random.randrange(1,4) + random.randrange(1,4),
    "Bard": random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Cleric" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Druid" : random.randrange(1,4)+ random.randrange(1,4),
    "Fighter" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Monk" : random.randrange(1,3),
    "Paladin" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Ranger" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Rouge" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Sorcerer" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Warlock" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4),
    "Wizard" : random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)+ random.randrange(1,4)
}
typeProficiencies = {
    "Barbarian" : "\n-Armor: \n   Light, Medium, Shields \n-Weapons: \n   Simple, Martial",
    "Bard" : "\n-Armor: \n   Light \n-Weapons: \n   Simple, Hand Crossbow, Longsword, Rapier, Shortswords \n-Tools: \n   3 Musical Instruments",
    "Cleric" : "\n-Armor: \n   Light, Medium, Shields \n-Weapons: Simple",
    "Druid" : "\n-Armor: \n   Light, Medium, Shields, No metal \n-Weapons: \n   Clubs, Daggers, Darts, Javelins, Maces, Quarterstaff, Scimitar, Sickles, Slings, Spears \n-Tools: \n   Hearbalism Kit",
    "Fighter" : "\n-Armor: \n   All armor and shields \n-Weapons: \n   Simple, Martial",
    "Monk" : "\n-Armor: \n   None \n-Weapons: \n   Simple, Shortswords \n-Tools: \n   1 Artisans tool or Instrument",
    "Paladin" : "\n-Armor: \n   All armor and shields \n-Weapons: \n   Simple Martial",
    "Ranger" : "\n-Armor: \n   Light, Medium, Shields \n-Weapons: \n   Simple Martial",
    "Rouge" : "\n-Armor: \n   Light \n-Weapons: \n   Simple, Hand Crossbow, Longsword, Rapier, Shortswords \n-Tools: \n   Thieves Tools",
    "Sorcerer" : "\n-Armor: \n   None \n-Weapons: \n   Dagger, Darts, Slings, Quarterstaff, Light Crossbow",
    "Warlock" : "\n-Armor: \n   Light \n-Weapons: \n   Simple",
    "Wizard" : "\n-Armor: \n   None \n-Weapons: \n   Daggers, Darts, Slings, Quarterstaff, Light Crossbow"
}
typeSavingThrows ={
    "Barbarian" : "\n-Strength, Constitution",
    "Bard" : "\n-Dexterity, Charisma",
    "Cleric" : "\n-Wisdom, Charisma",
    "Druid" : "\n-Intelligence, Wisdom",
    "Fighter" : "\n-Strength, Constitution",
    "Monk" : "\n-Strength, Dexterity",
    "Paladin" : "\n-Wisdom, Charisma",
    "Ranger" : "\n-Strength, Dexterity",
    "Rouge" : "\n-Dexterity, Intelligence",
    "Sorcerer" : "\n-Constitution, Charisma",
    "Warlock" : "\n-Wisdom, Charisma",
    "Wizard" : "\n-Intelligence, Wisdom"
}
skillProficiencies = {
    "Barbarian" : "\n-Choose 2 \n   Animal Handling, Athletics, Intimidation, Nature, Perception, Survival",
    "Bard" : "\n-Choose 3 \n   All skills avalible",
    "Cleric" : "\n-Choose 2 \n   History, Insight, Medicine, Persuasion, Religion",
    "Druid" : "\n-Choose 2 \n   Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival",
    "Fighter" : "\n-Choose 2 \n   Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, Survival",
    "Monk" : "\n-Choose 2 \n   Acrobatics, Athletics, History, Insight, Religion, Stealth",
    "Paladin" : "\n-Choose 2 \n   Athletics, Insight, Intimidation, Medicine, Persuasion, Religion",
    "Ranger" : "\n-Choose 3 \n   Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, Survival",
    "Rouge" : "\n-Choose 4 \n   Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Slight of Hand, Stealth",
    "Sorcerer" : "\n-Choose 2 \n   Arcana, Deception, Insight, Intimidation, Persuasion, Religion",
    "Warlock" : "\n-Choose 2 \n   Arcana, Deception, History, Intimidation, Investigation, Nature, Religion",
    "Wizard" : "\n-Choose 2 \n   Arcana, History, Insight, Investigation, Medicine, Religion"
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
gold = baseGold[type]

classProficiencies = typeProficiencies[type]
savingThrows = typeSavingThrows[type]
skills = skillProficiencies[type]

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
f.write("Proficiencies: " + str(classProficiencies) + "\n")
f.write("\n")
f.write("Saving Throw Proficiency: " + str(savingThrows) + "\n")
f.write("\n")
f.write("Skill Proficiencies: " + str(skills) + "\n")
f.write("\n")
f.write("Gold: " + str(gold) + "0" + "\n")
f.close()
