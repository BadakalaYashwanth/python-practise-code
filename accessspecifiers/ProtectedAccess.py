# Parent class
class Employee:

    # Constructor
    def __init__(self, name, salary):

        # Protected variables
        self._name = name
        self._salary = salary


    # Protected method
    def _show_details(self):

        print("\nEmployee Name:", self._name)

        print("Employee Salary:", self._salary)


# Child class inheriting Employee
class Developer(Employee):

    def display(self):

        # Accessing protected members
        self._show_details()


        # Condition statement
        if self._salary >= 50000:

            print("Senior Developer")

        else:

            print("Junior Developer")


# Creating object
dev = Developer("Yaswanth", 60000)


# Calling child method
dev.display()