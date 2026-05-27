import pandas as pd

student_Date = pd.DataFrame({
    "Name": ["Yashwanth", "Rahul", "Anish"],
    "Marks": [90, 93, 95]

})

# Printing original DataFrame
print("\nOriginal DataFrame\n")
print(student_Date)


# Deleting row with index 1
new_Data = student_Date.drop(1)

# Printing updated DataFrame
print("\nAfter Deleting Row\n")

print(new_Data)