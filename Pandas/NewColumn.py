# Import pandas
import pandas as pd

# Creating DataFrame
student_data = pd.DataFrame({

    "Name": ["Yaswanth", "Rahul", "Ansh"],
    "Marks": [90, 30, 85]
})

#Creating Empty List
result = []

#loop through the marks
for mark in student_data['Marks']:
    if mark >= 30:
        result.append("Pass")
    else:
        result.append("Fail")

# Adding new column
student_data["Result"] = result

#Printing result
print(student_data)

