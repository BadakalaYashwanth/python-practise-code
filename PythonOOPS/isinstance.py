# Parent class
class Employee:

    def work(self):

        print("\nEmployee works in company")


# Child class
class Developer(Employee):

    def coding(self):

        print("Developer writes Python code")


# Another child class
class Tester(Employee):

    def testing(self):

        print("Tester tests applications")


# Creating objects
dev = Developer()

test = Tester()


# Checking object types
print("\nChecking Developer Object")

print(isinstance(dev, Developer))

print(isinstance(dev, Employee))

print(isinstance(dev, Tester))


print("\nChecking Tester Object")

print(isinstance(test, Tester))

print(isinstance(test, Employee))

print(isinstance(test, Developer))