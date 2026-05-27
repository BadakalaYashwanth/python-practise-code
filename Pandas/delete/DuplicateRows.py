import pandas as pd

student_data = pd.DataFrame({
    "Name": ["Yashwanth", "Rahul", "Rahul"],
    "Marks": [90, 85, 85]
})

# Printing original DataFrame
print("\nOriginal DataFrame\n")

print(student_data)


# Removing duplicates
new_data = student_data.drop_duplicates()



# Printing updated DataFrame
print("\nAfter Removing Duplicates\n")

print(new_data)