import numpy as np

# STEP 1
# Create CSV file
file = open("sample.csv", "w")

# STEP 2
# Write data into CSV file
file.write("10,20,30\n")
file.write("40,50,60\n")
file.write("70,80,90\n")

# STEP 3
# Close file
file.close()
print("\nCSV File Created Successfully")

# STEP 4
# Read CSV file using NumPy
data = np.genfromtxt(
    "sample.csv",
    delimiter=","
)

# STEP 5
# Print data
print("\nData Loaded From CSV:\n")
print(data)


"""

Create CSV File
        ↓
Write Data
        ↓
Save File
        ↓
NumPy Reads CSV
        ↓
Convert Into Array
        ↓
Print Output


"""