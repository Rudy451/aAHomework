# Exercise 1 - Sum_To
def sum_to(n):
    if n == 1:
        return 1
    return n + sum_to(n - 1)

print("Exercise #1 - Tests")
print(sum_to(5))
print(sum_to(1))

# Exercise 2 - Add_Numbers
def add_numbers(nums_array):
    if len(nums_array) == 0:
        return None
    if len(nums_array) == 1:
        return nums_array[0]
    return nums_array[0] + add_numbers(nums_array[1:])

print("Exercise #2 - Tests")
print(add_numbers([1,2,3,4]))
print(add_numbers([3]))
print(add_numbers([-80,34,7]))
print(add_numbers([]))

# Exercise 3 - Gamma Function
def gamma_fnc(n):
    if n == 0:
        return None
    if n - 1 == 1 or n == 1:
        return 1
    return (n - 1) * gamma_fnc(n - 1)

print("Exercise #3 - Tests")
print(gamma_fnc(0))
print(gamma_fnc(1))
print(gamma_fnc(4))
print(gamma_fnc(8))

# Exercise 4 - Ice Cream Shop
def ice_cream_shop(flavors, favorite):
    if len(flavors) == 0:
        return False
    if flavors[0] == favorite:
        return True
    return ice_cream_shop(flavors[1:], favorite)

print("Exercise #4 - Tests")
print(ice_cream_shop(['vanilla', 'strawberry'], 'blue moon'))
print(ice_cream_shop(['pistachio', 'green tea', 'chocolate', 'mint chip'], 'green tea'))
print(ice_cream_shop(['cookies n cream', 'blue moon', 'superman', 'honey lavender', 'sea salt caramel'], 'pistachio'))
print(ice_cream_shop(['moose tracks'], 'moose tracks'))
print(ice_cream_shop([], 'honey lavender'))

# Exercise 5 - Reverse
def reverse(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    return reverse(string[1:]) + string[0]

print("Exercise #5 - Tests")
print(reverse("house"))
print(reverse("dog"))
print(reverse("atom"))
print(reverse("q"))
print(reverse("id"))
print(reverse(""))
