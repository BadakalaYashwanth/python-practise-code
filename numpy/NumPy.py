import numpy as np 
import time

list1 = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])

print("\nList Multiplication\n")
print([i * 2 for i in list1])

print("\nNumpy Multiplication\n")
print(arr * 2)