import copy
import math

from itertools import permutations

# Warmup
def my_recursive_range(start, end):
    if end < start:
        return []
    if start == end:
        return [start]
    return [start] + my_recursive_range(start + 1, end)

def my_iterative_range(start, end):
    my_array = []
    if end < start:
        return my_array
    for x in range(start, end + 1):
        my_array.append(x)
    return my_array

# range(1, 5)
print("Test #1 - Range(1, 5)")
print(my_recursive_range(1, 5))
print(my_iterative_range(1, 5))

# range(5, 1)
print("Test #2 - Range(5, 1)")
print(my_recursive_range(5, 1))
print(my_iterative_range(5, 1))

# Exponeniation
def exponent1(b, n):
    if n == 0:
        return 1
    return b * exponent1(b, n - 1)

def exponent2(b, n):
    if n == 0:
        return 1
    if n == 1:
        return b
    if n % 2 == 0:
        result = exponent2(b, n / 2)
        return result * result
    result = exponent2(b, (n - 1) / 2)
    return b * result * result

# recursion 1
#exp(b, 0) = 1
#exp(b, n) = b * exp(b, n - 1)
print("Test #1 - Simple Exponentiation")
print("Base  = 1, Power = 0-2")
print(exponent1(1, 0))
print(exponent1(1, 1))
print(exponent1(1, 2))
print("Base = 2, Power = 0-2")
print(exponent1(2, 0))
print(exponent1(2, 1))
print(exponent1(2, 2))
print("Base = 3, Power = 256")
print(exponent1(3, 256))

# recursion 2
#exp(b, 0) = 1
#exp(b, 1) = b
#exp(b, n) = exp(b, n / 2) ** 2             [for even n]
#exp(b, n) = b * (exp(b, (n - 1) / 2) ** 2) [for odd n]
#exp(b, 0) = 1
#exp(b, n) = b * exp(b, n - 1)
print("Test #2 - Simple Exponentiation")
print("Base  = 1, Power = 0-2")
print(exponent2(1, 0))
print(exponent2(1, 1))
print(exponent2(1, 2))
print("Base = 2, Power = 0-2")
print(exponent2(2, 0))
print(exponent2(2, 1))
print(exponent2(2, 2))
print("Base = 3, Power = 256")
print(exponent1(3, 256))

# Deep Dup
class new_list(list):

    def __init__(self, *args):
        self.list_elements = [element for element in locals()["args"]]

    def deep_dup(self, copy_list):
        if len(copy_list) == 1:
            return copy_list
        temp = copy_list[0]
        return [temp] + self.deep_dup(copy_list[1:])

    def __str__(self):
        return str(self.list_elements)

print("Deep Dup Test!")
my_list = new_list(1, [2], [3, [4]])
new_list = my_list.deep_dup(my_list.list_elements)
new_list[2] = 1
print(my_list, new_list)

# Fibonacci
def my_recursive_fibonacci(n):
    if n == 1:
        return [0, 1]
    result = my_recursive_fibonacci(n - 1)
    return result + [result[n - 1] + result[n - 2]]

def my_iterative_fibonacci(n):
    my_array = []
    for i in range(1, n + 1):
        if i == 1:
            my_array += [0, 1]
        else:
            my_array.append(my_array[i - 1] + my_array[i - 2])
    return my_array

# Recusive Test
print("Test #1 - Recursion")
print(my_recursive_fibonacci(10))

# Iterative Test
print("Test #2 - Iteration")
print(my_iterative_fibonacci(10))

# Binary Search
def bsearch(array, target):
    if len(array) == 1 and array[0] != target:
        return None
    if array[0] == target:
        return 0
    if array[int(len(array) / 2)] > target:
        return bsearch(array[0:int(len(array)/2)], target)
    else:
        result = bsearch(array[int(len(array)/2):len(array)], target)
        if result is None:
            return result
        else:
            return result + int(len(array) / 2)

# Binary Search Tests
print("Binary Search Tests!")
print(bsearch([1, 2, 3], 1))
print(bsearch([2, 3, 4, 5], 3))
print(bsearch([2, 4, 6, 8, 10], 6))
print(bsearch([1, 3, 4, 5, 9], 5))
print(bsearch([1, 2, 3, 4, 5, 6], 6))
print(bsearch([1, 2, 3, 4, 5, 6], 0))
print(bsearch([1, 2, 3, 4, 5, 7], 6))

# Merge Sort
def merge(array1, array2):
    new_array = []
    target = len(array1 + array2)
    while len(new_array) != target:
        empty_array1 = len(array1) == 0
        not_empty_array2 = len(array2) > 0
        if empty_array1 or (not_empty_array2 and (array1[0] > array2[0])):
            new_array.append(array2.pop(0))
        else:
            new_array.append(array1.pop(0))
    return new_array

def merge_sort(array):
    if len(array) == 1:
        return array
    return merge(merge_sort(array[0:int(len(array)/2)]), merge_sort(array[int(len(array)/2):len(array)]))

# Merge Sort Test
print("Merge Sort Test!")
print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4, 10, 20, 1, 22, 100, 1, 88]))

# Array Subsets
def subsets(array):
    if len(array) == 0:
        return [[]]
    list_1 = subsets(array[:-1])
    list_2 = copy.deepcopy(list_1)
    [my_list.append(array[-1]) for my_list in list_2]
    return list_1 + list_2

print("SubArrays Test!")
print(subsets([])) # => [[]]
print(subsets([1])) # => [[], [1]]
print(subsets([1, 2])) # => [[], [1], [2], [1, 2]]
print(subsets([1, 2, 3]))
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Permutations
def target_index_function(my_array):
    my_spot = len(my_array[len(my_array)-1])
    for spot in range(0, len(my_array)):
        if len(my_array[spot]) <= my_spot:
            return spot

def new_permutations(array, value=0, my_array=[], my_array_index=0):
    if len(array) == 1:
        my_array[my_array_index] += array
        my_array[my_array_index].insert(0, value)
        return 0
    if len(my_array) == 0:
        my_array = [[] for spot in range(0, math.prod(array))]
    my_array_index = target_index_function(my_array)
    for spot in array:
        spot_index = array.index(spot)
        result = array[0:spot_index] + array[spot_index+1:]
        new_permutations(result, array[spot_index], my_array, my_array_index)
        if value != 0:
            my_array[my_array_index].insert(0, value)
        my_array_index += 1
    return my_array

# Permutations Test
print("Permutation Test")
my_list = [1, 2, 3]
print(new_permutations(my_list))

# Make Change
def greedy_make_change(amount, coins=[25,10,5,1]):
    if amount - coins[0] == 0:
        return [coins[0]]
    if amount >= coins[0]:
        return [coins[0]] + greedy_make_change(amount - coins[0], coins)
    return greedy_make_change(amount, coins[1:])

# Greedy Change Test
print("Greedy Change Test!")
print(greedy_make_change(40, [25,10,5,1]))

def make_better_change(amount, coins=[25, 10, 5, 1]):
    if amount - coins[0] == 0:
        return [coins[0]]
    coin_selection = [[coin] + make_better_change(amount - coin, coins[coins.index(coin):]) for coin in coins if coin <= amount and coin <= coins[0]]
    coin_index = [len(coin_list) for coin_list in coin_selection]
    coin_index = coin_index.index(min(coin_index))
    return coin_selection[coin_index]

# Make Better Change Test
print("Make Better Change Test")
print(make_better_change(24, [10, 7, 1]))
