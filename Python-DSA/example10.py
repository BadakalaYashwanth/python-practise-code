from io import StringIO
import requests
import pandas as pd

# Access a publicly shared CSV file from Google Drive,
# read its contents into a Pandas DataFrame,
# and display the first few rows of the dataset.

csv_link = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

# Send a request to the Google Drive CSV link and retrieve the file content
response = requests.get(csv_link)

# Convert the downloaded CSV content into a file-like object
data_source = StringIO(response.text)

# Read the CSV data into a Pandas DataFrame
dataframe = pd.read_csv(data_source)

# Display the first 5 rows of the dataset
print(dataframe.head())