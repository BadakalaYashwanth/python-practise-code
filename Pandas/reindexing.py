# Import pandas
import pandas as pd

# Creating DataFrame
student_data = pd.DataFrame({
    "Name": ["Yaswanth", "Rahul", "Ansh"],
    "Marks": [90, 85, 75]
})

#Printing Original DataFrames
print("\nPrinting Origincal DataFrames")
print(student_data)

# Reindexing rows
new_Data = student_data.reindex([2, 0, 1])
print('\nReindexing rows')
print(new_Data)