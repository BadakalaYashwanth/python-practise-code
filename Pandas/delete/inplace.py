# Import pandas
import pandas as pd


# Creating DataFrame
student_data = pd.DataFrame({

    "Name": ["Yaswanth", "Rahul"],

    "Marks": [90, 85]
})


# Deleting row permanently
student_data.drop(1, inplace=True)


# Printing DataFrame
print(student_data)