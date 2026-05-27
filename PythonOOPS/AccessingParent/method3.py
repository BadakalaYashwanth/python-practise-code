#Parent Class
class Employee:
    def company(self):
        print("\nEmployee works in ABC Company")

#Child Class
class Developer(Employee):
    def show(self):

        #Calling parent Method
        Employee.company(self)
        print("Developer writes code")

#Creating object
dev = Developer()

#Calling method
dev.show()