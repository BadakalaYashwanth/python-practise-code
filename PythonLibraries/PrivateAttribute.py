# Class definition
# Class is blueprint for creating objects

class Student:


    # Constructor method
    # Automatically runs when object is created

    def __init__(self):


        # Private variable
        # Double underscore (__) makes variable private

        self.__salary = 50000



# Object creation
# Creating object of Student class

obj = Student()



# Accessing private variable using name mangling
# Python internally changes:
# __salary  →  _Student__salary

print(obj._Student__salary)