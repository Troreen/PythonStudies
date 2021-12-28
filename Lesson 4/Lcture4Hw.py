# Q1
# Topic: If-Else / For-Loop
# Points: 5
# -----------------------------------------------------------------------------
# o Write a program that asks the user to enter a number.
# o If the number is greater than 10, print "The number is greater than 10".
# o If the number is less than or equal to 10, print "The number is less than or equal to 10".
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q2
# Topic: If-Else / For-Loop / Lists / Functions
# Points: 20
# -----------------------------------------------------------------------------
# o Jim is in a forest. It's been quite some time he hasn't eaten anything. He knows that he will get hungry soon. He knows that this side of the forest is full of delicious mushrooms. But he also is not good distinguishing poisonous mushrooms from delicious mushrooms.
# o Every mushroom in the forest has a code on it, a string of letters. Luckily, he has a list of codes, if a mushroom includes any of these codes in it's code, then it is poisonous. He needs to however check the mushrooms quickly since he doesn't have much time left. We are going to write a program that will check which mushrooms are poisonous and which are not. And count how many mushrooms Jim can eat.
# o The function is_poisonous takes a mushroom code as an argument and returns True if the mushroom is poisonous and False if it is not.
# o The function count_poisonous takes a list of mushroom codes and returns the number of poisonous mushrooms in the list.
# Sample Input:
# poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
# forest_mushrooms = ['htrcd', 'tarpes', 'xxytr', 'ceaar', 'vvbctd', 'vsxz', 'accr', 'ccod', 'ttyt', 'garxxytacr', 'ccd', 'xz']
# Sample Output:
# The forest contains: 12 mushrooms
# Number of poisonous mushrooms: 6
# Number of edible mushrooms: 6
# -----------------------------------------------------------------------------
def is_poisonous(mushroom, poisonous_codes):
    # mushroom = arpe
    # poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
    for code in poisonous_codes:
        if code in mushroom:
            return True # poisonous
    return False # non-poisonous


def count_poisionous(mushroom_list, poisonous_codes):
    counter_p = 0
    for mushroom in mushroom_list:
        if is_poisonous(mushroom, poisonous_codes):
            counter_p = counter_p + 1
    return counter_p


poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
forest_mushrooms = ['htrcd', 'tarpes', 'xxytr', 'ceaar', 'vvbctd', 'vsxz', 'accr', 'ccod', 'ttyt', 'garxxytacr', 'ccd', 'xz']
num_p = count_poisionous(forest_mushrooms, poisonous_codes)
num_m = len(forest_mushrooms)

print(f'Total number of mushrooms:\t{num_m}')
print(f'Number of poisonous:\t\t{num_p}')
print(f'Number of edible:\t\t{num_m - num_p}')
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q3
# Topic: If-Else / Functions
# Points: 5
# -----------------------------------------------------------------------------
# o Write a function that takes the temprature as an argument and prints if user should go outside or not, and how the weather is. Use at least 3 different if-else statements.
# o Make up your own loagic about the weather.
# Sample Input:
# temprature = -35
# Sample Output:
# You should not go outside. It is freezing... Damn!
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q4
# Topic: If-Else / Functions / Lists
# Points: 5
# -----------------------------------------------------------------------------
# o Write a function that takes a list of numbers as an argument and returns the largest number in the list.
# o The function should return None if the list is empty.
# Sample Input:
# numbers = [1, 2, 3, 4, 5]
# Sample Output:
# 5
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q5
# Topic: If-Else / Functions / ?
# Points: 10
# -----------------------------------------------------------------------------
# o Write a function that takes hours as argument (as a float) and converts it to hours, minutes and seconds and prints it.
# Sample Input:
# hours = 1.53
# Sample Output:
# 1 hour 31 minutes and 48 seconds
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q6
# Topic: If-Else / Functions / Lists
# Points: 5
# -----------------------------------------------------------------------------
# o Write a function that converts a list of digits into a list of thier names.
# o The function should return None if the list is empty.
# Sample Input:
# numbers = [1, 2, 3, 4, 5]
# Sample Output:
# ['one', 'two', 'three', 'four', 'five']
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q7
# Topic: If-Else / Functions / ? / ?
# Points: 5
# -----------------------------------------------------------------------------
# o Write a function that takes in a string. The function should return True if the string is a palindrome and False if it is not.
# o A palindrome is a string that is the same forwards and backwards.
# o The function should return None if the string is empty.
# Sample Input:
# string = "racecar"
# Sample Output:
# True
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q8
# Topic: If-Else / For-Loop / Lists / Functions
# Points: 40
# -----------------------------------------------------------------------------
# o We want to create a partial to-do list. We want to be able to add new items to the list, remove items from the list, and mark items as completed. We then want to be able to print the list.
# o Create a function called add_item that takes in a list and a string. The function should add the string to the list.
# o Create a function called remove_item that takes in a list and a string. The function should remove the string from the list.
# o Create a function called mark_completed that takes in a list and a string. The function should mark the string as completed.
# o Create a function called print_list that takes in a list. The function should print the list.
# Sample Input:
# todo_list = ['wash car', 'buy groceries', 'pay bills']
# Sample Output:
# - wash car
# - buy groceries
# - pay bills
###
# Add an item to the list: 'go to the gym'
# Remove an item from the list: 'pay bills'
# Mark an item as completed: 'wash car'
# Run the program again to see the updated list.
# Sample Output:
# x wash car
# - buy groceries
# - go to the gym
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q9
# Topic: For-Loop / Lists / Functions
# Points: 15
# -----------------------------------------------------------------------------
# o Fibonacci numbers are numbers that follow the pattern: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# o Write a function that takes in a number n and returns the nth Fibonacci number.
# o The function should return None if the number is less than 1.
# Sample Input:
# n = 5
# Sample Output:
# 5
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Q10
# Topic: If-Else / Lists / Functions
# Points: 25
# -----------------------------------------------------------------------------
# o Write a function 'multiply_string' that takes in two strings and returns the product of the two strings.
# o The function should return None if the strings are empty.
# Constraints:
# o The strings should be integers.
# o Strings will be smaller than fifty (values 0 - 49).
# Sample Input:
# string1 = 'twenty two'
# string2 = 'three'
# Sample Output:
# 66
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# BONUS Q:
# Topic: ?
# Points: 100 (partial credit available)
# -----------------------------------------------------------------------------
# COMING SOON!