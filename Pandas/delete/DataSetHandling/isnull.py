# Import pandas
import pandas as pd
# Read CSV
data = pd.read_csv("address.csv")

# Check missing values
print("\nMissing Values Check\n")
#inull --> will detect the null values in the dataset
print(~data.isnull())

"""
| Output | Meaning       |
| ------ | ------------- |
| True   | Missing value |
| False  | Value exists  |
"""