import numpy as np

# Function to find nearest value
def find_nearest_value(arr, value):
    # Convert list into NumPy array
    arr = np.asarray(arr)
    # Find difference between array and target value
    difference = np.abs(arr - value)
    # Find index of smallest difference
    idx = difference.argmin()
    # Return nearest value
    return arr[idx]

# Original array
arr = np.array([
    0.21169,
    0.61391,
    0.6341,
    0.0131,
    0.16541,
    0.5645,
    0.5742
])

# Target value
value = 0.60
# Function call
result = find_nearest_value(arr, value)
print("\nNearest Value:\n")
print(result)

"""
| Function       | Purpose                                |
| -------------- | -------------------------------------- |
| `np.array()`   | Creates NumPy array                    |
| `np.asarray()` | Converts list into NumPy array         |
| `np.abs()`     | Converts negative values into positive |
| `argmin()`     | Returns index of smallest value        |



"""