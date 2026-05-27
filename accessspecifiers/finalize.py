#creating class
class Employee:

    # Constructor
    def __init__(self, name):        
        self.name = name,
        print("\nConstrcutor Called")
        
    # Destructor
    def __del__(self):
        print("Destructor Called")
        print("Memory Cleaned for: ", self.name)
    
empp = Employee("Yashwanth")
del empp