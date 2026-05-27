import pandas as pd

data = pd.read_csv("address.csv")
print("\nDataSet Statistics\n")
print(data.describe())

"""

| Information | Meaning            |
| ----------- | ------------------ |
| mean        | Average            |
| min         | Smallest           |
| max         | Largest            |
| std         | Standard deviation |



"""