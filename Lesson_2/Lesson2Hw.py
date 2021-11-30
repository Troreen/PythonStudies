'''
# Exercise 1
for i in range(2, 10):
    print(i+1)

# Exercise 2
for i in range(6):
    for j in range(1, i+1):
        print(j, "", end="")
    print("\r")

# Exercise 3
nums = [1]
limit = int(input("What number do you want to go up until?"))
for i in range(limit+1):
    nums.append(i)
total = sum(nums)
print(total)

# Exercise 4
num = int(input("Give a number"))
for i in range(11):
    print(num, "x", i, "=", i * num)

# Exercise 5
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

# Exercise 6
num = int(input("Enter number: "))
print(len(str(num)))

# Exercise 7
for i in range(6):
    for j in range(5, i, -1):
        print(j, "", end="")
    print("\r")
'''

