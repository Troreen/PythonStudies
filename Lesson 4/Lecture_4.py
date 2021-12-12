# Exercise 0
# 0: 
'''
print(5 < 3)
print("5" == 5)
print(55 == "55")
print(6 > 10)
print(2 == 3)
print(5 > 3)
print("5" != 5)
print(55 != "55")
print(6 < 10)
print(2 != 3)
'''
# Exercise 1
# 0:
names = ["Diana", "Bedir", "Tarik", "Jonas"]
def crowd_test(list):
    if len(list) > 3:
        print("The list is too crowded")
    elif len(list) == 3:
        print("Perfect!")
    else: 
        print("It's a bit too short isn't it?")
crowd_test(names)
names.remove("Jonas")
crowd_test(names)

# 1:
# did in the answer of the first one

# 2:
names1 = ["Diana", "Bedir", "Tarik", "Jonas", "Nilgun", "Huzeyfe"]
def crowd_test1(list):
    if len(list) > 5:
        print("There is a damn mob in here!")
    elif len(list) > 2:
        print("This room is crowded")
    elif len(list) == 1 or len(list) == 2:
        print("Pretty empty room.")
    else: 
        print("There is literally no one in here.")
crowd_test1(names1)

# Exercise 2
# Q1:
    # Make a list of ten aliens, each of which is one color: 'red', 'green', or 'blue'.
    # You can shorten this to 'r', 'g', and 'b' if you want, but if you choose this option you have to include a comment explaining what r, g, and b stand for.
    # Red aliens are worth 5 points, green aliens are worth 10 points, and blue aliens are worth 20 points.
    # Use a for loop to determine the number of points a player would earn for destroying all of the aliens in your list.
# Q2:
# 20 points
# There are three groups of people in a class. The first group is the teacher, the second group is the students, and the third group is the parents.
    # The teacher is worth 5 points, the students are worth 10 points, and the parents are worth 15 points.
    # Use a for loop to determine the total number of points the class would earn if all groups were to give all of their points.
    # If a student is missing their parents, they should not be counted.
    # Make sure to include a comment exp
    # Input sample:
    # - [t, t, p1, p2, p4, p6, s1, s2, s5, s4, s3]
    # Output:
    # - 100

lss = ["t", "t", "p1", "p2", "p4", "p6", "s1", "s2", "s5", "s4", "s3"]

def calculate_points(ls):
    points = 0
    for i in ls:
        if i == "t": points += 5
        elif "p" in i:
            if "s"+i[1] in ls:
                points += 25
            else:
                points += 15
    print(points)
calculate_points(lss)