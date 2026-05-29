# List of student tuples
# Each tuple contains:
# (Name, Marks)

students = [
    ("Yashwanth", 90),
    ("Rahul", 80),
    ("Anil", 95)
]


# sort() is built in list method
# Used to sort elements in list

# key=
# Defines custom sorting rule

# lambda x: x[1]
# Lambda creates temporary function

# x represents each tuple one by one

# First iteration:
# x = ("Yashwanth", 90)

# x[1]
# Access second value from tuple
# Result = 90

# Second iteration:
# x = ("Rahul", 80)

# x[1]
# Result = 80

# Third iteration:
# x = ("Anil", 95)

# x[1]
# Result = 95


# Python collects:
# 90, 80, 95

# Then sorts using these values


students.sort(key=lambda x: x[1])


# Print final sorted list
print("\nSorted Students Based On Marks:\n")

print(students)


""" 
Sorted Students Based On Marks:

[
 ('Rahul', 80),
 ('Yashwanth', 90),
 ('Anil', 95)
]
"""