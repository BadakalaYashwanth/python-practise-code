# Import pandas library
import pandas as pd

# Create first Series
series_A = pd.Series([2, 4, 8, 10, 12])

# Create second Series
series_B = pd.Series([8, 10, 12, 15, 16])

# Check whether values from series_A
# exist inside series_B
check_values = series_A.isin(series_B)

print("\nChecking Matching Values\n")
print(check_values)

# Filter only matching values
result = series_A[series_A.isin(series_B)]


# Print final result
print("\nCommon Values Present in Both Series\n")

print(result)