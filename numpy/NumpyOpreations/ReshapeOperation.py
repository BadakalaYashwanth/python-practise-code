import numpy as np

arr = np.array([1, 2, 3, 5, 6, 7 ])

new_Arr = arr.reshape(3, 2)
print("\nReshpae\n", new_Arr)

"""
Example:
we have 6 elements in the arr 

Rows × Columns
must equal
Total Elements

6 elements

2 × 3 = 6
3 × 2 = 6
1 × 6 = 6
6 × 1 = 6


"""