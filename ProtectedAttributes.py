class Student:
    def __init__(self):
        self.name = "Yashwanth"
        self.age = 23
        self.__salary = 50000

    def get_salary(self):
        return self.__salary 

student = Student()
print(student.get_salary())  # ✅ Prints 50000
