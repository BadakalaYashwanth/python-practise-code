import numpy as np

# Original array
inputArray = np.array([
    [35, 53, 63],
    [72, 12, 22],
    [43, 84, 56]
])
print("\nOriginal Array:\n")
print(inputArray)


# Delete first column
arr = np.delete(inputArray, 0, axis=1)
#     np.insert(array_name, index, axis)
print("\nAfter Deleting First Column:\n")
print(arr)

# New column
new_col = np.array([20, 30, 40])

# Insert new column
arr = np.insert(arr, 0, new_col, axis=1)
#     np.insert(array_name, index, values, axis)
print("\nFinal Array:\n")
print(arr)