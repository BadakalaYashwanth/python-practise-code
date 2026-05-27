"How many rows and columns are present in the array"

import numpy as np


# 2D Array
arr_two_dim = np.array([
    ["x1", "x2", "x3", "x4"],
    ["x5", "x6", "x7", "x8"]
])

# 1D Array
arr_one_dim = np.array([3, 2, 4, 5, 6])


# Print arrays
print("\n2D Array:\n")
print(arr_two_dim)


print("\n1D Array:\n")
print(arr_one_dim)


# Find shape using .shape
print("\nShape of 2D Array:\n")
print(arr_two_dim.shape)



print("\nShape of teh 1D Array:\n")
print(arr_one_dim.shape)