CHEESES=["cheddar", "gouda", "camembert"]
def roll_call_dwarves(dwarves):
    i=1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    return[f"{call.title()}!" for call in planeteer_calls]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
        
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return food

    return None
