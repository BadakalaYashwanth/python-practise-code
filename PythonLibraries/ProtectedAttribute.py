# Class definition
# Class is blueprint for creating objects

class Student:


    # Constructor method
    # Automatically runs when object is created

    def __init__(self):


        # Protected variable
        # Single underscore (_) means protected

        self._name = "Yashwanth"



# Object creation
# Creating object of Student class

obj = Student()


# Accessing protected variable
# Protected variables CAN still be accessed outside class
# But developers should avoid direct access

print(obj._name)