# Import pandas
import pandas as pd


# Read CSV
data = pd.read_csv("address.csv")


# Dataset information
print("\nDataset Information\n")

print(data.info())