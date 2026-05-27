# Import pandas
import pandas as pd

# Read CSV
data = pd.read_csv("address.csv")

# Print datatypes
print("\nColumn Datatypes\n")

print(data.dtypes)