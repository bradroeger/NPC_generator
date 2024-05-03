# modern_professions.py

# Define the era name as a module-level variable
era_name = "Modern"

poor_professions = [
    "homeless person", "street vendor", "fast food worker", "delivery driver"
]

working_class_professions = [
    "factory worker", "construction worker", "retail worker", "janitor", "nurse"
]

middle_class_professions = [
    "engineer", "accountant", "manager", "software developer, doctor"
]

upper_class_professions = [
    "CEO", "investor", "celebrity", "politician"
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