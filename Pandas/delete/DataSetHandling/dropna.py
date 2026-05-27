# Import pandas
import pandas as pd


# Read CSV
data = pd.read_csv("address.csv")


# Remove rows containing missing values
clean_data = data.dropna()


# Print cleaned data
print(clean_data)