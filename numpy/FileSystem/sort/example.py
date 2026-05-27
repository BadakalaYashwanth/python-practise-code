import numpy as np

# Original array
arr = np.array([
    [8, 3, 2],
    [3, 6, 5],
    [6, 1, 4]
])

print("\nOriginal Array:\n")
print(arr)

# Sort using second column
sorted_arr = arr[arr[:, 1].argsort()]
print("\nSorted Array Based On Second Column:\n")
print(sorted_arr)