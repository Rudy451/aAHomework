def sum_integers(array):
    if len(array) == 1:
        return array[0]
    return array[0] + sum_integers(array[1:])

print("Problem 1: You have array of integers. Write a recursive solution to find the sum of the integers.")
print(sum_integers([1, 2, 3, 4, 5]))

def recurring_integers(array, target):
    if len(array) == 1:
        return 1 if array[0] == target else 0
    return (1 if array[0] == target else 0) + recurring_integers(array[1:], target)

print("Problem 2: You have array of integers. Write a recursive solution to determine whether or not the array contains a specific value.")
print(recurring_integers([1, 2, 2, 4, 5], 2))

def unsorted_recurring_integers(array, target):
    array.sort()
    return recurring_integers(array, target)

print("Problem 3: You have array of integers. Write a recursive solution to determine whether or not the array contains a specific value.")
print(unsorted_recurring_integers([5, 1, 2, 4, 5], 5))

def sum_adjacent_integers(array, target):
    if len(array) == 2:
        return array[0] + array[1] == target
    return array[0] + array[1] == target or sum_adjacent_integers(array[1:], target)

print("Problem 4: You have array of integers. Write a recursive solution to determine whether or not two adjacent elements of the array add to 12.")
print(sum_adjacent_integers([5, 1, 2, 4, 5], 12))
print(sum_adjacent_integers([5, 4, 2, 6, 7, 5], 12))

def confirm_sorted_array(array):
    if len(array) == 2:
        return array[0] <= array[1]
    return array[0] <= array[1] and confirm_sorted_array(array[1:])

print("Problem 5: You have array of integers. Write a recursive solution to determine if the array is sorted.")
print(confirm_sorted_array([5, 1, 2, 4, 5]))
print(confirm_sorted_array([2, 3, 4, 5]))

def reverse_string(word):
    if len(word) == 1:
        return word[0]
    return word[-1] + reverse_string(word[:-1])

print("Problem 6: Write a recursive function to reverse a string. Don't use any built-in #reverse methods!")
print(reverse_string("House"))
