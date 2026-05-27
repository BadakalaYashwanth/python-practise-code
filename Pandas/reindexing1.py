# Import pandas
import pandas as pd


# Creating DataFrame
student_data = pd.DataFrame({

    "Name": ["Yaswanth", "Rahul"],

    "Marks": [90, 85]
})


# Adding new indexes
new_data = student_data.reindex([0, 1, 2, 3])


# Printing result
print(new_data)