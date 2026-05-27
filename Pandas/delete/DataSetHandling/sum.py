# Import pandas
import pandas as pd
# Read CSV
data = pd.read_csv("address.csv")
# Count missing values
print("\nMissing Value Count\n")

print(data.isnull().sum())