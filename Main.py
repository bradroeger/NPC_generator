import random
import os

selected_era = os.environ["SELECTED_ERA"]
import importlib


# Get the filename from user input or any other source
filename = selected_era

# Remove the ".py" extension if present
if filename.endswith(".py"):
    module_name = filename[:-3]
else:
    module_name = "eras." + filename

# Import the module dynamically
module = importlib.import_module(module_name)

poor_professions = module.poor_professions

working_class_professions = module.working_class_professions

middle_class_professions = module.middle_class_professions

upper_class_professions = module.upper_class_professions

if filename == "Victorian":
    factories = {
        'cotton mill': ["spinning", "weaving", "dyeing"],
        'steel mill': ["forging", "casting", "rolling"],
        "brewery": ["brewing", "bottling", "packing"],
        "pottery": ["throwing", "firing", "glazing"]
    }

#gender selector
genders_list = ["male"] * 40 + ["female"] * 40 + ["non-binary"] * 10 + ["trans"] * 10

#trans selector
trans_list = ["male"] * 50 + ["female"] * 50

#sexuality selector
sexuality_list = ["heterosexual"] * 80 + ["homosexual"] * 7 + ["bisexual"] * 7 + ["pansexual", "omnisexual"] * 3 + ["asexual"] * 3

#racial selector
racial_list = ["asian"] * 10 + ["african"] + 10 * ["european"] * 10 + ["middle eastern"] * 10 + ["latin american"] * 10 + ["native american"] * 10

def generate_sexuality():
    return random.choice(sexuality_list)

def generate_gender():
    return random.choice(genders_list)

def generate_trans():
    return random.choice(trans_list)

def generate_race():
     return random.choice(racial_list)

def generate_species(kingdom_class):
     return random.choice(species_list[kingdom_class])

gender = generate_gender()

if gender == "trans":
     gender = "trans " + generate_trans() 

# Race Subtypes
human_subtypes = ["dwarf", "human", "goliath"]
goblinoid_subtypes = ["goblin", "orc", "bugbear", "firbolg", "hobgoblin", "verdun"]
touched_subtypes = ["air", "earth", "fire", "water", "celestial", "infernal", "fae", "shadow"]
amphibious_subtypes = ["Frog",
    "Toad",
    "Salamander",
    "Newt",
    "Axolotl",
    "Caecilian",
    "Mudskipper",
    "Siren",
    "Hellbender",
    "Tree Frog",
    "Bullfrog",
    "Dart Frog",
    "Fire Salamander",
    "Mudpuppy"]
avian_subtypes = ["Eagle",
    "Hawk",
    "Falcon",
    "Owl",
    "Raven",
    "Crow",
    "Swan",
    "Dove",
    "Pigeon",
    "Sparrow",
    "Starling",
    "Magpie",
    "Vulture",
    "Seagull",
    "Parrot",
    "Peacock",
    "Hummingbird",
    "Pelican",
    "Albatross",
    "Penguin"]
furred_subtypes = ["Wolf",
    "Bear",
    "Lion",
    "Tiger",
    "Panther",
    "Fox",
    "Lynx",
    "Cheetah",
    "Jaguar",
    "Leopard",
    "Badger",
    "Wolverine",
    "Otter",
    "Raccoon",
    "Sable",
    "Ferret",
    "Weasel",
    "Marten",
    "Mink",
    "Skunk"]
scaled_subtypes = ["Snake",
    "Lizard",
    "Crocodile",
    "Monitor Lizard",
    "Gecko",
    "Iguana",
    "Chameleon",
    "Komodo Dragon",
    "Anaconda",
    "Boa Constrictor",
    "Python",
    "Cobra",
    "Viper",
    "Gila Monster"]
smooth_subtypes =["Rhino",
    "Hippo",
    "Elephant",
    "Buffalo",
    "Giraffe",
    "Horse",
    "Zebra",
    "Donkey",
    "Tapir",
    "Antelope",
    "Camel",
    "Okapi",
    "Warthog",
    "Bison",
    "Yak",
    "Moose",
    "Ox",
    "Gazelle",
    "Walrus",
    "Seal"]
beastkin_subtypes = ["amphibious", 
                     "avian", 
                     "furred",
                     "scaled",
                     "smooth"
]
species_list ={"amphibious": amphibious_subtypes,
                "avian": avian_subtypes,
                "furred": furred_subtypes,
                "scaled": scaled_subtypes,
                "smooth": smooth_subtypes
}
# Races and their subtypes for the generator
races = {
    "human": human_subtypes,
    "beastkin": beastkin_subtypes,
    "korrigan": [],
    "goblinoid": goblinoid_subtypes,
    "touched": touched_subtypes
}

economic_levels = ["poor", "working-class", "middle-class", "upper-class"]

# Define age range
min_age = 12
max_age = 89

# Personality type dictionary don't need to edit this section really just call what you need.
personality_types = {
    "ISTJ": {
        "description": "The Inspector",
        "traits": "Introverted, Sensing, Thinking, Judging",
        "strengths": "Honest, Direct, Strong-willed, Dutiful, Responsible, Practical",
        "weaknesses": "Inflexible, Stubborn, Judgmental, Harsh, Unreasonably Blame Themselves",
    },
    "ISFJ": {
        "description": "The Protector",
        "traits": "Introverted, Sensing, Feeling, Judging",
        "strengths": "Supportive, Reliable, Patient, Imaginative, Observant, Loyal",
        "weaknesses": "Humble, Shy, Overload Themselves, Repress Their Emotions, Too Altruistic",
    },
    "INFJ": {
        "description": "The Counselor",
        "traits": "Introverted, Intuitive, Feeling, Judging",
        "strengths": "Creative, Insightful, Inspiring and Convincing, Decisive, Determined, Altruistic",
        "weaknesses": "Sensitive, Extremely Private, Perfectionistic, Always Need to Have a Cause",
    },
    "INTJ": {
        "description": "The Mastermind",
        "traits": "Introverted, Intuitive, Thinking, Judging",
        "strengths": "Quick-witted, Intelligent, Strategic and Visionary, High Self-Confidence, Independent",
        "weaknesses": "Arrogant, Judgmental, Overly Analytical, Loathe Highly Structured Environments",
    },
    "ISTP": {
        "description": "The Craftsman",
        "traits": "Introverted, Sensing, Thinking, Perceiving",
        "strengths": "Bold, Practical, Creative, Rational, Calm, Practical",
        "weaknesses": "Insensitive, Private, Reserved, Easily Bored, Risky Behavior",
    },
    "ISFP": {
        "description": "The Composer",
        "traits": "Introverted, Sensing, Feeling, Perceiving",
        "strengths": "Charming, Sensitive, Artistic, Independent, Friendly, Quiet",
        "weaknesses": "Easily Stressed, Overly Competitive, Struggle to Make Tough Decisions, Dislike Conflict",
    },
    "INFP": {
        "description": "The Healer",
        "traits": "Introverted, Intuitive, Feeling, Perceiving",
        "strengths": "Empathetic, Idealistic, Creative, Passionate, Altruistic, Strong Beliefs",
        "weaknesses": "Too Idealistic, Impractical, Dislike Dealing with Data, Take Things Personally",
    },
    "INTP": {
        "description": "The Architect",
        "traits": "Introverted, Intuitive, Thinking, Perceiving",
        "strengths": "Intellectual, Logical, Objective, Cool-headed, Curious, Independent",
        "weaknesses": "Insensitive, Absent-minded, Condescending, Obsessive, Can be Too Focused on Theory",
    },
    "ESTP": {
        "description": "The Dynamo",
        "traits": "Extraverted, Sensing, Thinking, Perceiving",
        "strengths": "Energetic, Confident, Adaptable, Bold, Resourceful, Hands-on",
        "weaknesses": "Impulsive, Insensitive, Risk-taking, Unstructured, May Neglect Planning",
    },
    "ESFP": {
        "description": "The Performer",
        "traits": "Extraverted, Sensing, Feeling, Perceiving",
        "strengths": "Enthusiastic, Outgoing, Friendly, Playful, Spontaneous, Good at Improvisation",
        "weaknesses": "Poor Long-term Planning, Impulsive, Overly Focused on Present, Overly Emotional, May Struggle with Criticism",
    },
    "ESTJ": {
        "description": "The Executive",
        "traits": "Extraverted, Sensing, Thinking, Judging",
        "strengths": "Organized, Efficient, Strategic, Responsible, Dependable, Confident",
        "weaknesses": "Can be Inflexible, Impatient, Overly Focused on Results, May Struggle with Emotional Support",
    },
    "ESFJ": {
        "description": "The Provider",
        "traits": "Extraverted, Sensing, Feeling, Judging",
        "strengths": "Warm-hearted, Social, Empathetic, Generous, Responsible, Conscientious",
        "weaknesses": "May Struggle with Change, Difficulty with Conflict, Overly Focused on Social Status, May Struggle with Decision-making",
    },
    "ENTP": {
        "description": "The Debater",
        "traits": "Extraverted, Intuitive, Thinking, Perceiving",
        "strengths": "Quick-witted, Clever, Energetic, Charismatic, Creative, Resourceful",
        "weaknesses": "Argumentative, Insensitive, Intolerant, Easily Bored, Poor Follow-through",
    }
}

ethnicity = ""

# Generate a random NPC
human_weight = 60  # Adjust this weight according to your preference
total_other_races = len(races) - 1  # Subtract 1 for human race
other_race_weight = (100 - human_weight) / total_other_races
total_races = len(races)
race_weights = [human_weight if race == "human" else other_race_weight for race in races]
race = random.choices(list(races.keys()), weights=race_weights)[0]

if race == "human":
    ethnicity = generate_race()

if race == "touched":
    ethnicity = generate_race()


subtype = random.choice(races[race]) if races[race] else None
economic_level = random.choice(economic_levels)

if race == "beastkin":
    ethnicity = generate_species(subtype)


if economic_level == "poor":
    profession = random.choice(poor_professions)
elif economic_level == "working-class":
    profession = random.choice(working_class_professions)
elif economic_level == "middle-class":
    profession = random.choice(middle_class_professions)
else:
    profession = random.choice(upper_class_professions)
if selected_era == "Victorian":
    if profession == "factory worker":
        factory = random.choice(list(factories))
        task = random.choice(factories[factory])
        profession_total = f"{profession} ({task} at {factory})"


# Define personality type weights for each profession
profession_personality_weights = {
    "apprentice": {"ISTJ": 0.3, "ESTJ": 0.2, "ISFJ": 0.2, "ESFJ": 0.1, "ESTP": 0.1, "ISTP": 0.1},
    "bootblack": {"ISTJ": 0.4, "ESTJ": 0.3, "ISFJ": 0.2, "ESFJ": 0.1},
    "costermonger": {"ESTP": 0.4, "ISTP": 0.3, "ESFP": 0.2, "ISFP": 0.1},
    "factory worker": {"ISTJ": 0.4, "ESTJ": 0.3, "ISFJ": 0.2, "ESFJ": 0.1},
    "porter": {"ISTJ": 0.3, "ESTJ": 0.2, "ISFJ": 0.2, "ESFJ": 0.1, "ESTP": 0.1, "ISTP": 0.1},
    "seamstress": {"ISTJ": 0.3, "ISFJ": 0.3, "ESFJ": 0.2, "ESTJ": 0.1, "ISFP": 0.1},
    "charwoman": {"ISTJ": 0.4, "ISFJ": 0.3, "ESFJ": 0.2, "ESTJ": 0.1},
    "clerk": {"ISTJ": 0.6, "ISFJ": 0.2, "ESTJ": 0.2},
    "constable": {"ISTJ": 0.7, "ISFJ": 0.3},
    "footman": {"ISFJ": 0.6, "ESFJ": 0.3, "ISTJ": 0.1},
    "housemaid": {"ISFJ": 0.6, "ESFJ": 0.3, "ISTJ": 0.1},
    "laundry maid": {"ISFJ": 0.5, "ESFJ": 0.4, "ISTJ": 0.1},
    "milkmaid": {"ISFJ": 0.6, "ESFJ": 0.4},
    "nursemaid": {"ISFJ": 0.7, "ESFJ": 0.3},
    "parlormaid": {"ISFJ": 0.6, "ESFJ": 0.3, "ISTJ": 0.1},
    "policeman": {"ISTJ": 0.7, "ISFJ": 0.3},
    "scullery maid": {"ISFJ": 0.5, "ESFJ": 0.4, "ISTJ": 0.1},
    "servant": {"ISFJ": 0.6, "ESFJ": 0.3, "ISTJ": 0.1},
    "tailor": {"ISFP": 0.6, "ESFP": 0.4 },
    "valet": {"ISTJ": 0.2, "ESTJ": 0.1, "ISFJ": 0.4, "ESFJ": 0.3 },
    "waiter": {"ISTJ": 0.1, "ESTJ": 0.1, "ISFJ": 0.2, "ESFJ": 0.6 },
    "waitress": {"ISTJ": 0.1, "ESTJ": 0.1, "ISFJ": 0.3, "ESFJ": 0.5 },
    "butler": {"ISTJ": 0.4, "ESTJ": 0.2, "ISFJ": 0.3, "ESFJ": 0.1 },
    "governess": {"ISTJ": 0.2, "ESTJ": 0.1, "INTJ": 0.3, "INFJ": 0.4 },
    "housekeeper": {"ISTJ": 0.3, "ESTJ": 0.2, "ISFJ": 0.4, "ESFJ": 0.1 },
    "shopkeeper": {"ISTJ": 0.3, "ESTJ": 0.4, "ISFJ": 0.2, "ESFJ": 0.1 },
    "noble": {"ISTJ": 0.3, "ESTJ": 0.3, "INTJ": 0.2, "INFJ": 0.2 },
    "priest": {"INFJ": 0.6, "ENFJ": 0.4 },
    "sailor": {"ISTP": 0.4, "ESTP": 0.3, "ISFP": 0.2, "ESFP": 0.1 },
    "thief": {"ISTP": 0.6, "ESTP": 0.3, "ISFP": 0.1 },
    "wizard": {"INTP": 0.4, "ENTP": 0.4, "INTJ": 0.2 }
}

# Choose a personality type based on profession weights
if profession in profession_personality_weights:
    weights = profession_personality_weights[profession]
    personality_type = random.choices(list(weights.keys()), weights=list(weights.values()))[0]
else:
    # If profession not found, choose a random personality type
    personality_type = random.choice(list(personality_types))

age = random.randint(min_age, max_age)

# Print out the NPC's attributes
print(module.era_name)
print(f"Race: {race}")
if subtype:
    print(f"Subtype: {subtype}")
print(race)
if race == "human" or race == "touched":
    print(f"Ethnicity: {ethnicity}")  
if race == "beastkin":
    print(f"Class:  {ethnicity}")  
print(f"Gender: {gender}")
print(f"Economic Level: {economic_level}")
print(generate_sexuality())
if profession == "factory worker":
	print(f"Profession: {profession_total}")
else:
	print(f"Profession: {profession}")
print(f"Personality Type: {personality_type}")
print("Description:", personality_types[personality_type]["description"])
print("Traits:", personality_types[personality_type]["traits"])
print("Strengths:", personality_types[personality_type]["strengths"])
print("Weaknesses:", personality_types[personality_type]["weaknesses"])
print(f"Age: {age}")