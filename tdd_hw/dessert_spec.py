import unittest

from dessert import Dessert

class DessertTests(unittest.TestCase):

    def initialize_test(self):
        # initialize test object
        my_dessert = Dessert("cupcake", 10, "Gordon Ramsey")

        # sets a type
        self.assertEqual(my_dessert.type_of, "cupcake")

        # sets a quanity
        self.assertEqual(my_dessert.quantity, 10)

        # starts ingredients as empty array
        self.assertCountEqual(my_dessert.ingredients, [])

        # raises an argument error when given a non-integer quantity
        my_dessert = Dessert("cupcake", "10", "Gordon Ramsey")
        with self.assertRaises(AttributeError) as test_error:
            my_dessert.quantity
        print("Failed as expected.")

    def add_ingredient_test(self):
        # adds ingredient to the ingredients array
        my_dessert = Dessert("cupcake", 10, "Gordon Ramsey")
        self.assertEqual(my_dessert.add_ingredient("flour"), ["flour"])


    def mix_test(self):
        # shuffles the ingredient array
        my_dessert = Dessert("cupcake", 10, "Gordon Ramsey")
        my_dessert.add_ingredient("flour")
        my_dessert.add_ingredient("sugar")
        my_dessert.add_ingredient("milk")
        my_dessert.mix()
        self.assertNotEqual(my_dessert.ingredients, ["flour", "sugar", "milk"])


    def eat_test(self):
        # substracts an amount from the quantity
        my_dessert = Dessert("cupcake", 10, "Gordon Ramsey")
        my_dessert.eat(2)
        self.assertEqual(my_dessert.quantity, 8)

    def serve_test(self):
        # contains the titleized version of the chef's name
        my_dessert = Dessert("cupcake", 10, "Gordon Ramsey")
        self.assertEqual(my_dessert.serve(), "Chef Gordon Ramsey the Great Baker has made 10 cupcakes")

    def make_more_test(self):
        # calls bake on the dessert's chef with the dessert passed in
        my_dessert = Dessert("cupcake", 10, "Gordon Ramsey")
        my_dessert.add_ingredient("flour")
        my_dessert.add_ingredient("sugar")
        my_dessert.add_ingredient("milk")
        my_dessert.chef.bake(my_dessert)
        self.assertEqual(my_dessert.temp, 400)

my_test = DessertTests()
my_test.initialize_test()
my_test.add_ingredient_test()
my_test.mix_test()
my_test.eat_test()
my_test.serve_test()
my_test.make_more_test()
