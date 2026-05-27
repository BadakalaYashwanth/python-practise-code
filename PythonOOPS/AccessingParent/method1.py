#Using Child Object
#Parent Class 
class Employee:
    def company(self):
        print("\nEmployee works in ABC Company")

#Child Class
class Developer(Employee):
    def coding(self):
        print("\nDeveloper writes in Python")

#Creating Child Object
dev = Developer()

#Accessing parent Class
dev.company() # Child object accessing parent method directly

# Accessing child method
dev.coding()