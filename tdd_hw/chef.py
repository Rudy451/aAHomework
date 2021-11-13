class Chef:

    def __init__(self, name):
        self.name = name

    def titleize(self):
        return "Chef " + self.name + " the Great Baker"

    def bake(self, dessert):
        dessert.mix()
        self.__put_in_oven(dessert)

    def __put_in_oven(self, dessert):
        dessert.heat()
