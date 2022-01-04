# Q1
# Topic: If-Else / For-Loop
# Points: 5
# -----------------------------------------------------------------------------
# o Write a program that asks the user to enter a number.
# o If the number is greater than 10, print "The number is greater than 10".
# o If the number is less than or equal to 10, print "The number is less than or equal to 10".
# -----------------------------------------------------------------------------
num = int(input("Enter a number: "))
if num > 10: print("The numb er is greater than 10")
else: print("The number is less than or equal to 10")
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
temp = int(input("Enter the temprature: "))
if temp > 15 : print("It's a nice weather.")
elif temp > 0: print("You should put on a jacket or a coat.")
elif temp > -10: print("You have to make sure your clothes protect you from the cold.")
else: print("You should probably cancel your plans.")
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
numbers = []
for i in range(5):
    new_number = input("Enter numbers here: ")
    numbers.append(new_number)
numbers.sort(reverse = True)
print(f"The largest number is: {numbers[0]}")

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
digits_txt = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def converter(list):
    new_ls = []
    for item in list:
        new_ls.append(digits_txt[digits.index(item)])
    print(new_ls)
numbers = [1,4,2,t5]
converter(numbers)
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
def palindrome(string):
    if string == string[::-1]: return True
    else: return False
print(palindrome("racecar"))
print(palindrome("nah"))
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
def add_item(list, list_done):
    item = input("Enter item you want to add: ")
    list.append(item)

def remove_item(list, list_done):
    item = input("Enter item you want to remove: ")
    list.remove(item)
    if item in list_done:
        list_done.remove(item)

def mark_completed(list, list_done):
    item = input("Enter item you want to mark completed: ")
    list_done.append(item)

def print_list(list):
    for item in list:
        if item in done_list:
            print(f"x {item}")
        else:
            print(f"- {item}")

done_list = []
todo_list = ['wash car', 'buy groceries', 'pay bills']
add_item(todo_list, done_list)
remove_item(todo_list, done_list)
mark_completed(todo_list, done_list)
print_list(todo_list)

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
def fibonacci():
    n1 = 0
    n2 = 1
    limit = int(input())
    if limit < 0:
        print("Incorrect input")
    elif limit == 1:
        print(n1+1)
    elif limit == 2:
        print(n2)
    else:
        for i in range(1,limit): 
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        print(n2)
fibonacci()

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
numbers_txt = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen", "twenty", "thirty", "forty"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40]
def multiply_string(string1, string2):
    if not string1 or not string2:
        return None
    elif " " in string1:
        string1 = string1.split(" ")
        num1 = numbers[numbers_txt.index(string1[0])] + numbers[numbers_txt.index(string1[1])]
    elif " " not in string1:
        num1 = numbers[numbers_txt.index(string1)]
    if " " in string2:
        string2 = string2.split(" ")
        num2 = numbers[numbers_txt.index(string2[0])] + numbers[numbers_txt.index(string2[1])]
    elif " " not in string2:
        num2 = numbers[numbers_txt.index(string2)]
    return(num1*num2)
        
print(multiply_string("twenty two","three"))
print(multiply_string("","ten"))

# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# BONUS Q:
# Topic: ?
# Points: 100 (partial credit available)
# -----------------------------------------------------------------------------
# COMING SOON!
