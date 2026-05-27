# ==============================
# NUMERIC DATA TYPES
# ==============================

# Integer data type
a = 10

# Float data type
b = 10.5

# Complex number data type
c = 2 + 3j

# Boolean data type
d = True

print("\nValue of a:", a)
print("Purpose: Stores whole numbers")
print("Data type of a:", type(a))

print("\nValue of b:", b)
print("Purpose: Stores decimal numbers")
print("Data type of b:", type(b))

print("\nValue of c:", c)
print("Purpose: Stores complex numbers")
print("Data type of c:", type(c))

print("\nValue of d:", d)
print("Purpose: Stores True or False values")
print("Data type of d:", type(d))


# ==============================
# SEQUENCE DATA TYPES
# ==============================

# List data type
numbers = [1, 2, 3]

print("\nList values:", numbers)
print("Purpose: Stores multiple values and allows modification")
print("Data type:", type(numbers))

# Tuple data type
data = (1, 2, 3)

print("\nTuple values:", data)
print("Purpose: Stores multiple fixed values")
print("Data type:", type(data))

# String data type
name = "Python"

print("\nString value:", name)
print("Purpose: Stores text data")
print("Data type:", type(name))


# ==============================
# RANGE DATA TYPE
# ==============================

numbers = range(5)

print("\nRange values:")
print("Purpose: Generates sequence of numbers")

for i in numbers:
    print(i)

print("Data type:", type(numbers))


# ==============================
# DICTIONARY DATA TYPE
# ==============================

student = {
    "name": "Yaswanth",
    "age": 22
}

print("\nDictionary:", student)
print("Purpose: Stores data in key-value pairs")

# Accessing dictionary value
print("Student name:", student["name"])

print("Data type:", type(student))


# ==============================
# SET DATA TYPE
# ==============================

numbers = {1, 2, 3, 3}

print("\nSet values:", numbers)
print("Purpose: Stores unique values only")

# Duplicate value automatically removed
print("Data type:", type(numbers))


# ==============================
# NONE TYPE
# ==============================

x = None

print("\nValue of x:", x)
print("Purpose: Represents no value or null value")
print("Data type:", type(x))


# ==============================
# FUNCTION / CALLABLE TYPE
# ==============================

def greet():
    print("Hello")

print("\nPurpose: Functions are callable objects")
print("Calling greet() function:")

greet()


# ==============================
# MODULE USAGE
# ==============================

import math

print("\nPurpose: math module provides mathematical functions")

print("Square root of 16:", math.sqrt(16))


# ==============================
# isinstance() FUNCTION
# ==============================

x = 10

print("\nValue of x:", x)

# Check if x is float
print("Is x a float?", isinstance(x, float))

# Check if x is int
print("Is x an int?", isinstance(x, int))

print("Purpose: isinstance() checks whether variable belongs to a specific data type")