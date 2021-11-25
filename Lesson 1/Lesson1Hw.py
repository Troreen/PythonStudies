# HW:
# - Write a program that uses everything you have learned in this notebook at least once.
# - Write comments that label each section of your program.
# - For each thing your program does, write at least one line of comment that explains what your program did.

# Setting a variable "text" that has a sentence with whitespaces on both sides which are being removed with
# the use of String Functions strip(), lstrip(), and rstrip()
# I am also using concatenation by printing two strnig variables together 
# we are also using the string function .capitalize() to have our text printed out with a capital letter in the start
text = "    hELLO " 
text2 = "wOrLd-               "
print(text + text2)
print(text.strip())
print(text.lstrip())    
print(text.rstrip())
print((text + text2).strip().title())

# In this part of our code we will be doing mathematical operations by taking input from the user
print("Hey, in this part of the program you as the user get to contribute as well, you get to choose 2 numbers to do mathematical operatoins with.")
num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
# Printing out the things the user can do with the numbers they gave
print("Now choose what you want to do with these numbers: ") 
print("1.", num1, "+", num2)    
print("2.", num1, "-", num2)
print("3.", num1, "/", num2)
print("4.", num1, "*", num2)
print("5.", num1, "^", num2)   

# Taking input from the user to determine what they want to do with the
# numbers they gave earlier according to the options given to them
operation = input() 
# Using the input that we just took from the user to do mathematical operations
if operation == "1":    # Using if statements and putting the answer in a variable
    answer = num1 + num2
elif operation == "2":
    answer = num1 - num2
elif operation == "3":
    answer = num1 // num2
elif operation == "4":
    answer = num1 * num2
elif operation == "5":
    answer = num1 ** num2
print("The answer is", answer)  # Printing out the answer