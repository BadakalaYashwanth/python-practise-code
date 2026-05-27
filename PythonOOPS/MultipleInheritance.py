#Parent class
class Teacher:
    def subject(self):
        print("\nThe Teacher Explaining in the Python")

#child class
class Trainee:
    def training(self):
        print("\nThe Traine explaining the paratical code")

#child class
class student(Trainee, Teacher):
    def check(self, marks):
        self.marks = marks

        for mark in marks:

            if mark >= 32:
                print("PASS")
            else:
                print("Fail")
                
# Creating object                
Student1 = student()

# Calling parent methods
Student1.subject()

Student1.training()

Student1.check([20, 50, 70, 10])