class Map:

    def __init__(self):
        self.it_map = []

    def set(self, key, value):
        check = True
        for pair in self.it_map:
            if pair[0] == key:
                pair[1] = value
                check = False
                break
        if check:
            self.it_map.append([key, value])

    def get(self, key):
        for pair in self.it_map:
            if pair[0] == key:
                return pair[1]
        return "Value Not Found"

    def delete(self, key):
        new_array = []
        for spot in range(0, len(self.it_map)):
            if self.it_map[spot][0] == key:
                pass
            else:
                new_array.append(self.it_map[spot])
        self.it_map = new_array

# Create stack instance
my_map = Map()

# Add new elements to map
my_map.set("TB", 10)
my_map.set("TB", 12)
my_map.set("AR", 12)
my_map.set("RW", 3)

# Get map element
print(my_map.get("TB"))

# Delete map element
my_map.delete("RW")
print(my_map.get("RW"))
