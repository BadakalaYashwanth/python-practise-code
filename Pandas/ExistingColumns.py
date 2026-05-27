# Import pandas
import pandas as pd

# Creating DataFrame
employee_data = pd.DataFrame({

    "Salary": [50000, 60000, 70000]
})

# Adding bonus column
employee_data["Bonus"] = employee_data["Salary"] * 12

# Printing result
print(employee_data)