# Spell Jammer Professions

# Define the era name as a module-level variable
era_name = "Spelljammer"

poor_professions = [
"asteroid miner", "cargo loader", "cleaner", "janitor", "mechanic", "scavenger"
]

working_class_professions = [
"astroengineer", "astrologer", "astromechanic", "astrosurveyor", "buccaneer", "cook",
"gunner", "helmsman", "navigator", "pilot", "shipwright", "smuggler", "spacerigger",
"technician", "trader", "voidfarer", "weapon master"
]

middle_class_professions = [
"arcane architect", "artificer", "bounty hunter", "explorer", "inquisitor", "merchant",
"mercenary", "missionary", "privateer", "prospector", "researcher", "scout", "spelljammer",
"spymaster"
]

upper_class_professions = [
"archmage", "consort", "diplomat", "high priest", "king/queen", "lord/lady", "navigator"
"navigator-princeprincess", "psion", "regent", "sage", "space captain", "warlord",
"weapons merchant", "wizard-king/queen"
]

def generate_profession(economic_level):
    if economic_level == "poor":
        profession = random.choice(poor_professions)
    elif economic_level == "working-class":
        profession = random.choice(working_class_professions)
    elif economic_level == "middle-class":
        profession = random.choice(middle_class_professions)
    else:
        profession = random.choice(upper_class_professions)
    return profession