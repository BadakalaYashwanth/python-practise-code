# Import pandas library
import pandas as pd


# Creating student data
data = {

    "Name": ["Yaswanth", "Rahul", "Ansh", "Kiran"],

    "Age": [22, 21, 23, 20],

    "Marks": [85, 30, 90, 40]
}


# Creating DataFrame
df = pd.DataFrame(data)


# Printing full DataFrame
print("\nComplete Student Data\n")

print(df)


# Accessing single column
print("\nStudent Names\n")

print(df["Name"])


# Condition filtering
print("\nStudents Who Passed\n")

passed_students = df[df["Marks"] >= 35]

print(passed_students)


# Adding new column
df["Result"] = ["Pass", "Fail", "Pass", "Pass"]


# Printing updated DataFrame
print("\nUpdated DataFrame\n")

print(df)


# Loop through rows
print("\nStudent Report\n")

for index, row in df.iterrows():

    print("\nName:", row["Name"])

    print("Marks:", row["Marks"])

    print("Result:", row["Result"])