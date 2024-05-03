# Space Professions

# Define the era name as a module-level variable
era_name = "Space"

poor_professions = [
"asteroid miner", "cargo loader", "cleaner", "janitor", "mechanic", "sanitation worker", "scavenger"
]

working_class_professions = [
"astroengineer", "astrogeologist", "astromechanic", "astrosurveyor", "cargo pilot", "cargo hauler",
"engineer", "helmsman", "mechanical technician", "mining technician", "orbital construction worker",
"pilot", "security officer", "shipyard worker", "smuggler", "space marine", "spacerigger",
"technician", "transporter operator"
]

middle_class_professions = [
"asteroid prospector", "bounty hunter", "explorer", "freighter captain", "interstellar diplomat",
"merchant", "missionary", "privateer", "researcher", "scout", "space archaeologist", "space lawyer",
"space medic", "space psychologist", "trader", "xenobiologist"
]

upper_class_professions = [
"artificial intelligence developer", "celebrity space explorer", "CEO of a space corporation",
"cyberneticist", "diplomat", "empire administrator", "high priest of a space religion", "intergalactic politician",
"media mogul", "navigator-prince/princess", "philanthropist", "space tourism magnate",
"space tycoon", "super soldier", "terraforming engineer"
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