# Import pandas
import pandas as pd

# Read CSV
data = pd.read_csv("address.csv")


# Replace missing values with Unknown
data["City"] = data["City"].fillna("Unknown")


# Print updated dataset
print(data)