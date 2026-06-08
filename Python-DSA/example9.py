from collections import Counter

# Create the first dictionary containing key-value pairs
data_list = {'key1': 50, 'key2': 100, 'key3': 200}

# Create the second dictionary containing key-value pairs
data_list_c1 = {'key1': 200, 'key2': 100, 'key4': 300}

# Convert both dictionaries to Counter objects
# and add the values of common keys together
new_dict = Counter(data_list) + Counter(data_list_c1)

# Display the resulting dictionary
print(new_dict)