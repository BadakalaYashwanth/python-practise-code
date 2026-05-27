# Import pandas
import pandas as pd

# Creating DataFrame
student_data = pd.DataFrame({
    "Name": ["Yaswanth"],
    "Marks": [90]
})

# Reindexing columns
new_data = student_data.reindex(columns=['Marks', 'Name'])
print(new_data)