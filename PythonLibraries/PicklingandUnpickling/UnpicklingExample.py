# Import pickle module
import pickle


# Open file in read binary mode
# rb = read binary
file = open("student.pkl", "rb")


# pickle.load()
# Reads binary data
# Converts back to Python object
student = pickle.load(file)


# Close file
file.close()


print("\nLoaded Data:\n")
print(student)