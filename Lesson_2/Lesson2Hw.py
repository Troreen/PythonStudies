'''
    # Exercise 1
for i in range(2, 10):
    print(i+1)

# Exercise 2 
for i in range(6):
    for j in range(1, i+1):
        print(j, "", end="")
    print("")

# Exercise 3
nums = [1]
limit = int(input("What number do you want to go up until?: "))
for i in range(limit+1):
    nums.append(i)
total = sum(nums)
print(total)

# Exercise 4
num = int(input("Give a number: "))
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

# Exercise 8
list = [1, 2, 3, 4, 5]
for i in reversed(list):
    print(i)

# Exercise 9
for i in range(-10, 0):
    print(i)

# Exercise 10
fav_bands = ["Leyla the Band", "Duman", "Milky chance", "YYK", "Mor ve Otesi"]
for i in range(fav_bands):
    print(i)

# Exercise 11
n = int(input("Give limit: "))
for num in range (2, n + 1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# Exercise 12
n1 = 0
n2 = 1
for i in range(11): 
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

# Exercise 13
n = int(input("What number do you want to find the factorial of?: "))
sum = 1
for i in range(1, n + 1):
    sum = sum * i
print("!" + str(n), "=", sum)

# Exercise 14
n = int(input("Give number: "))
reverse = 0
while n > 0:
    reminder = n % 10
    reverse = reverse * 10 + reminder
    n //= 10
print(reverse)

# Exercise 15
list = [0, 1, 2, 3, 4, 5]
for i in list[1::2]:
    print(i)

# Exercise 16
num = int(input("Give limit: "))
for i in range(num+1):
    print(i,"^ 3 =", i**3)

# Exercise 17
n = int(input("Up to how many terms?: "))
t = "2"
sum = 0
for i in range(1, n+1):
    sum = sum + int(t*i)
print(sum)

# Exercise 18
for i in range(6):
    for j in range(1, i+1):
        print("* ", end="")
    print("")
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("* ", end="")
    print("")
'''
