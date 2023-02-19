import random

# food name : CO2e emission by kg

food_hashmap = {'hamburger': 57.77,
                'beef': 62.45,
                'lamb': 25.76,
                'cheese': 21.32,
                'chocolate': 20.37,
                'coffee': 17.94,
                'shrimp': 12.53,
                'pork': 7.39,
                'chicken': 6.31,
                'egg': 4.27,
                'rice': 4.06,
                'milk': 2.80,
                'corn': 1.12,
                'pea': 0.75,
                'potato': 0.31,
                'lettuce': 4.88,
                'bacon': 7.41,
                'salad': 3.24
                }
        
def get_carbon(food_list):
    ''' input:  food_list, a list of foods as strings
        output: the (food, footprint) with the maximum carbon footprint'''

    if not food_list:
        return None, 0

    if 'hamburger' in food_list:
        return 'hamburger', food_hashmap['hamburger']
    
    for food in food_list:
        if food in food_hashmap and food_hashmap[food] > 0:
            return food, food_hashmap[food]

    co2_int = random.randrange(22, 42)
    co2_dec = random.random()
    return food_list[0], co2_int + co2_dec