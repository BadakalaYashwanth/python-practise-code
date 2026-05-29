# Import pickle module
import pickle


# Python dictionary object
student = {
    "name": "Yaswanth",
    "age": 22,
    "course": "Python"
}


# Open file in write binary mode
# wb = write binary

file = open("student.pkl", "wb")


# pickle.dump()
# Saves Python object into file

pickle.dump(student, file)


# Close file
file.close()


print("\nData Saved Successfully")