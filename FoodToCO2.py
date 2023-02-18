# food name : CO2e emission by kg

class FoodToCO2:
    def __init__(self):
        self.food_hashmap = {'hamburger': 3.24,
                             }
        
    def get_carbon(self, food_list):
        ''' input:  food_list, a list of foods as strings
            output: the food with the maximum carbon footprint'''
        curr_max = 0
        curr_food = None

        for food in food_list:
            if food in self.food_hashmap:
                if self.food_hashmap[food] > curr_max:
                    curr_max = self.food_hashmap[food]
                    curr_food = food

        if curr_food: return curr_food
        return None