import re

# Function to convert a date from YYYY-MM-DD format
# to DD-MM-YYYY format using regular expressions
def transform_date_format(date):

    # Search for a date in the format YYYY-MM-DD
    # (\d{4}) captures the year
    # (\d{1,2}) captures the month
    # (\d{1,2}) captures the day
    # Replace it with Day-Month-Year format
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)


# Input date in YYYY-MM-DD format
date_input = "2021-08-01"

# Convert the date format and display the result
print(transform_date_format(date_input))