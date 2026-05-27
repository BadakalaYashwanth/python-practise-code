# Import pandas
import pandas as pd


# Import numpy
import numpy as np


# Creating first Series
series_A = pd.Series([2, 4, 5, 8, 10])


# Creating second Series
series_B = pd.Series([8, 10, 13, 15, 17])


# Step 1:
# Combine both Series
union_values = pd.Series(np.union1d(series_A, series_B))

print("\nUnion Values\n")

print(union_values)


# Step 2:
# Find common values
common_values = pd.Series(np.intersect1d(series_A, series_B))

print("\nCommon Values\n")

print(common_values)


# Step 3:
# Remove common values from union
result = union_values[~union_values.isin(common_values)]

print("\nNon Common Values\n")

print(result)