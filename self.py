class student:

    def __init__(self, name):
        self.name = name
    def show(self):
        print("Name:", self.name)


s = student("Adarsh")
s.show()