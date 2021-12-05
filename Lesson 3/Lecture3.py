# Exercise 1
# 0:
list = [x * 10 for x in range(1, 11) ]
print(list)

# 1:
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

# 2:
names = ["Tarik", "Diana", "Jonas", "Nilgun", "Yusuf"]
awesome_names = [awesome.title() + " is awesome" for awesome in names]
print(awesome_names)

# Exercise 
# 0:
def greeting(name):
    print(f"Hello {name}\nMerry Christmas {name}\nYou are loved {name}")

greeting("Tarik")
# 1:
def full_name(first, last):
    first = input("What is your name? ")
    last = input("What is your lastname? ")
    print(f"Hello, {first} {last}.")

full_name(first=input, last=input)


# 2:
def adding(n1, n2):
    n1 = int(input("Give the first number: "))
    n2 = int(input("Give the second number: "))
    print(f"Adding {n1} and {n2} will be equal to {n1+n2}.")
adding()