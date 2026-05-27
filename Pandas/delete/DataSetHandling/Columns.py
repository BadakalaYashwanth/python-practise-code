# Import pandas
import pandas as pd


# Read CSV
data = pd.read_csv("address.csv")


# Print column names
print("\nColumn Names\n")

print(data.columns)