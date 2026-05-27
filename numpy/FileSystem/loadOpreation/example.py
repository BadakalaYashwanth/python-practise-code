import numpy as np
# STEP 1
# Create a text file
file = open("data.txt", "w")

# STEP 2
# Write numbers into the file
file.write("10 20 30\n")
file.write("40 50 60\n")
file.write("70 80 90\n")

# STEP 3
# Close the file
file.close()
print("\nText file created successfully")



# STEP 4
# Read the file using NumPy 
data = np.loadtxt("data.txt")


# STEP 5
# Print the loaded data
print("\nData loaded from file:\n")
print(data)