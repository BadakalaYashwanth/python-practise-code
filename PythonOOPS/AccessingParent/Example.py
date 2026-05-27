#Parent Class
class Employee:
    def company(self):
        print("\nEmployee belongs to ABC Company")

#Child Class
class Developer(Employee):
    def check(self, tasks):
        #Accessing the Parent Class
        super().company()

        for task in tasks:
            if task >= 5:
                print("Completed Task", task)
            else:
                print("Pending Task", task)
#Creating Object
dev = Developer()
dev.check([4,7,2,8,3,4,6,2,7])