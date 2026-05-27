# Import pandas
import pandas as pd

#First DataFrames
df1 = pd.DataFrame({
    "Name": ["Yashwanth", "Gowthami"],
})

# Second DataFrame
df2 = pd.DataFrame({
    'Marks': [98, 93]
})

result = pd.concat([df1, df2], axis=1)
print(result)