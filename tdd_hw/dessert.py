import copy
import inflect
import random

word = inflect.engine()

from chef import Chef

class Dessert:

    def __init__(self, type_of, quantity, chef):
        try:
            assert type(quantity) == int
            self.type_of = type_of
            self.quantity = quantity
            self.chef = Chef(chef)
            self.ingredients = []
            self.temp = 60
        except AssertionError:
            print("Quantity entered is not an integer")

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self.ingredients

    def mix(self):
        try:
            assert len(self.ingredients) > 0
            old_list = copy.deepcopy(self.ingredients)
            while old_list == self.ingredients:
                random.shuffle(self.ingredients)
        except AssertionError:
            print("No ingredients")

    def heat(self):
        self.temp = 400

    def eat(self, amount):
        try:
            assert (self.quantity - amount) > 0
            self.quantity -= amount
        except AssertionError:
            print("Not enough left!")

    def serve(self):
        return self.chef.titleize() + " has made " + str(self.quantity) + " " + word.plural(self.type_of)
