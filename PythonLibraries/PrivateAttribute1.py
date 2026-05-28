# Class definition
# Class is blueprint for creating objects

class Student:


    # Constructor method
    # Automatically called when object is created

    def __init__(self):


        # Private variable
        # Double underscore (__) makes variable private

        self.__salary = 50000
    

    # Method inside class
    # Used to access private variable safely

    def show_salary(self):


        # Print heading
        print("\nSalary\n")


        # Accessing private variable inside class
        # Private variables CAN be accessed inside same class

        print(self.__salary)



# Object creation
# Creating object of Student class

obj = Student()


# Calling class method using object
# Method prints private salary variable

obj.show_salary()