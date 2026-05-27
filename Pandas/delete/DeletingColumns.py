import pandas as pd 

student_Data = pd.DataFrame({
    "Name": ["Yashwnath", "Rahul"],
    "Marks": [90, 94],
    "Age": [23, 34]
})

# Printing original DataFrame
print("\nOriginal DataFrame\n")

print(student_Data)

# Deleting column
new_Data = student_Data.drop("Age", axis=1)
# Printing updated DataFrame
print("\nAfter Deleting Column\n")

print(new_Data)
