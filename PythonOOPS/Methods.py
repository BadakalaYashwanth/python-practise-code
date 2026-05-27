# Creating class
class Numbers:

    # Constructor
    def __init__(self, numbers):

        self.numbers = numbers


    # Method
    def display(self):

        # Loop
        for num in self.numbers:

            print(num)


# Creating object
obj = Numbers([1, 2, 3, 4])


# Calling method
obj.display()