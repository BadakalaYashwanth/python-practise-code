# Parent class
class Employee:

    pass


# Child class
class Developer(Employee):

    pass


# Another child class
class Tester(Employee):

    pass


# Checking inheritance
print("\nDeveloper inherits Employee:")

print(issubclass(Developer, Employee))


print("\nTester inherits Employee:")

print(issubclass(Tester, Employee))


print("\nEmployee inherits Developer:")

print(issubclass(Employee, Developer))