# Import copy module
import copy


# Original list
student = [
    "Yashwanth",
    ["Python", "React"]
]


# Create deep copy
student_copy = copy.deepcopy(student)
#Creates complete copy.
#Copies nested objects too.

print("\nBefore Modification:\n")

print(student)

print(student_copy)


#Modify nested list 
student_copy[1].append("Nodejs")
#Changes only copied list.
#Original remains untouched.


print("\nAfter Modification:\n")

print(student)

print(student_copy)