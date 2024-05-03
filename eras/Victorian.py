# Victorian Professions

# Define the era name as a module-level variable
era_name = "Victorian"

poor_professions = [
    "apprentice", "bootblack", "costermonger", "factory worker", "porter", "seamstress",
    "matchstick maker", "chimney sweep", "coal miner", "dock worker", "fruit picker", 
    "glass blower", "mechanic", "shoemaker", "tailor", "weaver", "cotton spinner", 
    "lace maker", "washerwoman", "chambermaid", "charwoman", "scullery maid",
    "potato peeler", "groom", "stable boy", "tinkerer", "inventor", "street vendor", 
    "sanitation worker", "clockmaker", "metalworker"
]

working_class_professions = [
    "airship crew member", "mechanic", "police officer", "detective", "librarian",
    "scribe", "nurse", "healer", "seamstress or tailor", "messenger", "milkman or milkwoman",
    "baker", "brewer", "butcher", "candle maker", "carpenter", "blacksmith", "coachman",
    "driver", "farrier", "groom", "gardener", "mason", "painter", "plumber", "printer",
    "sailor", "shoemaker", "tinsmith", "wheelwright", "wizard's assistant", "automaton operator"
]

middle_class_professions = [
    "accountant", "architect", "banker", "bookseller", "chemist", "clerk", "doctor",
    "engineer", "inventor", "journalist", "lawyer", "merchant", "photographer", 
    "printer", "professor", "publisher", "shopkeeper", "surveyor", "teacher", 
    "theater manager", "travel agent"
]

upper_class_professions = [
    "aristocrat", "banker", "baron", "barrister", "bishop", "captain", "countess",
    "duke", "duchess", "earl", "governor", "industrialist", "inventor", "judge",
    "landowner", "magistrate", "minister", "philanthropist", "physician", "polymath",
    "professor", "reverend", "sir", "spy", "viscount", "wizard"
]

# Define a dictionary that maps factory workers to factories
factories = {
    'cotton mill': ["spinning", "weaving", "dyeing"],
    'steel mill': ["forging", "casting", "rolling"],
    "brewery": ["brewing", "bottling", "packing"],
    "pottery": ["throwing", "firing", "glazing"]
}

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