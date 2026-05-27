#parent class
class Employee:
    def company(self):
        print("\nEmployee works in ABC Company")

#Child Class
class Developer(Employee):
    def show(self):
        #super() is used to access parent class members inside child class
        #Accessing the Parent class
        super().company()
        print("Developer writes code")

#Creating object
dev = Developer()

#Calling Child Method
dev.show()