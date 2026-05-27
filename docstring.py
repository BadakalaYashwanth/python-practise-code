class Student:
    """
    This class stores student information
    """
    def __init__(self, name, age):
        self.name = name   # public
        self.age = age     # public
        self.__name = "Private_" + name # private member

    def _display(self):
        print("Protected method called")

    def __display(self):
        print(self.name)
        print(self.age)
student = Student("Alice", 20)

# Accessing public members
print(student.name)
print(student.age)

print("\nAccessing private method:")
student._Student__display()

print("\nProtected members:")
student._display()

print("\nPrivate members:")
print(student._Student__name)