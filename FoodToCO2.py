# food name : CO2e emission by kg

food_hashmap = {'hamburger': 143.26,
                             'beef': 155.51,
                             'tofu': 0.80,
                             'banana': 1.15,
                             'apple': 0.63,
                             'chicken': 18.23,
                             'pork': 24.37
                             }
        
def get_carbon(food_list):
    ''' input:  food_list, a list of foods as strings
        output: the (food, footprint) with the maximum carbon footprint'''

    if not food_list:
        return None, 0

    if 'hamburger' in food_list:
        return 'hamburger', food_hashmap['hamburger']
    
    for food in food_list:
        if food in food_hashmap:
            return food, food_hashmap[food]

    return None, 0