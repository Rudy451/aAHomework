tiles_array = ["up", "right-up", "right", "right-down", "down", "left-down", "left",  "left-up" ]

# Slow Dance
def linear_search(target, array):
    result = None
    for move in range(0, len(array)):
        if array[move] == target:
            result = move
            break
    return result

print(linear_search("up", tiles_array))
print(linear_search("right-down", tiles_array))

# Constant Dance

tiles_array = {"up": 0, "right-up": 1, "right": 2, "right-down": 3, "down": 4, "left-down": 5, "left": 6, "left-up": 7}
def constant_search(target, hash):
    return hash[target]

print(constant_search("up", tiles_array))
print(constant_search("right-down", tiles_array))
