# Import pandas
import pandas as pd

# Read CSV file
data = pd.read_csv(
    "address.csv"
)

# Print first 5 rows
print("\nDataset Preview\n")
print(data.head())