# Import copy module
import copy

# Original list
student = [
    "Yashwanth",
    ["Python", "React"]
]

# Create shallow copy
student_copy = copy.copy(student)
#Creates shallow copy, Copies outer list only.

print("\nBefore Modification:\n")

print(student)
print(student_copy)


student_copy[1].append("NodeJS") #Adds item to nested list.

print("\nAfter Modification")
print(student)
print(student_copy)