class student:

    def __init__(self, marks):

        self.marks = marks
    
    def check(self):

        for mark in self.marks:

            if mark > 35:
                print("\nPass", mark)
            else:
                print("\nFail", mark)
student = student([20, 50, 70, 10])
student.check()