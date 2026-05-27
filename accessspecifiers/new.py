# Parent class
class Employee:

    def work(self):

        print("\nEmployee works on company tasks")


# Child class
class Developer(Employee):

    # Hiding parent method
    def work(self):

        print("Developer writes Python code")


# Creating parent object
emp = Employee()

# Creating child object
dev = Developer()


# Calling parent method
emp.work()


# Calling child method
dev.work()