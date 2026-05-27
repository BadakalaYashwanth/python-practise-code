# Import pandas
import pandas as pd


# First DataFrame
df1 = pd.DataFrame({

    "Name": ["Yaswanth", "Rahul"],

    "Marks": [85, 75]
})


# Second DataFrame
df2 = pd.DataFrame({

    "Name": ["Ansh", "Kiran"],

    "Marks": [90, 40]
})


# Combining DataFrames vertically
result = pd.concat([df1, df2])


# Printing result
print("\nCombined DataFrame\n")

print(result)