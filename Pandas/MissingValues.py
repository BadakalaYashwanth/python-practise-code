# Import pandas
import pandas as pd

# Import numpy
import numpy as np


# Creating DataFrame with missing values
student_data = pd.DataFrame({

    "Name": ["Yaswanth", "Rahul", "Ansh", "Kiran"],

    "Marks": [90, np.nan, 85, np.nan]
})


# Printing original DataFrame
print("\nOriginal DataFrame\n")

print(student_data)

# Checking missing values
#True = if missing the value
#False = if value is present
print("\nChecking Missing Values\n")
print(student_data.isnull())


#Calculating the Mean
print("\nMean Value")
mean_value = student_data["Marks"].mean()
print(mean_value)



# Filling missing values with mean
print("\nFilling missing values with mean")
student_data['Marks'] =student_data["Marks"].fillna(mean_value)
print(student_data)