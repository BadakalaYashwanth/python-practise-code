# Import pandas
import pandas as pd


# Dictionary
marks = {

    "Yaswanth": 85,

    "Rahul": 30,

    "Ansh": 90
}


# Creating Series
students = pd.Series(marks)


# Condition check
print("\nPassed Students\n")


for name, mark in students.items():

    if mark >= 35:

        print(name, "Passed")