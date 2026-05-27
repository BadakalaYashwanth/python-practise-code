import numpy as np
ndArray = np.array([1, 2, 3, 4], ndmin=6)
print(ndArray)
print('\nDimensions of array: \n', ndArray.ndim)


"""
ndmin means:
minimum dimensions
NumPy creates array with at least 6 dimensions

"""