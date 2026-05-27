class Student:

    def __init__(self):

        self.__salary = 50000


student = Student()

# Direct access causes error
# print(student.__salary)

print("\nPrivate attribute cannot be accessed directly")