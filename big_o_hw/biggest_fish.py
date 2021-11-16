import copy

fish = ['fish', 'fiiish', 'fiiiiish', 'fiiiish', 'fffish', 'ffiiiiisshh', 'fsh', 'fiiiissshhhhhh']

# Sluggish Octopus
def bubble_sort(array):
    for x in range(0, len(array)):
        for y in range(0, len(array)):
            if len(array[y]) > len(array[x]):
                temp = copy.deepcopy(array[x])
                array[x] = copy.deepcopy(array[y])
                array[y] = temp
    return array[len(array) - 1]

print(bubble_sort(fish))

# Dominant Octopus
def merge(array1, array2):
    new_array = []
    for val in array1 + array2:
        if len(new_array) == 0:
            new_array.append(val)
        elif len(val) >= len(new_array[len(new_array) - 1]):
            new_array.append(val)
        else:
            new_array.insert(0, val)
    return new_array

    return
def merge_sort(array, n):
    if len(array) == 1:
        return array
    else:
        new_array = merge(merge_sort(array[0:int(len(array)/2)], n), merge_sort(array[int(len(array)/2):], n))
        return new_array[len(new_array) - 1] if len(new_array) == n else new_array
print(merge_sort(fish, len(fish)))

# Clever Octopus
def clever_sort(array):
    val = ""
    for sub_val in array:
        if len(sub_val) > len(val):
            val = sub_val
    return sub_val

print(clever_sort(fish))
