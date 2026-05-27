class EmployeeDetails:
    # Constructor function
    def __init__(self, name, age, Job_Role, Job_Id, salary):
        self.name = name
        self.age = age
        self.Job_Role = Job_Role
        self.Job_Id = Job_Id
        self.salary = salary
    
    #Method inside class
    def result(self):
        print(f'The Name of the Employee is {self.name} and age is {self.age} with job title {self.Job_Role} and salary is {self.salary} and Employee Id is {self.Job_Id}')

    def check_bonus(self):
        
        if self.salary >= 5000:
            print("\n", self.name, "is eligible for bonus")
        else:
            print("\n", self.name, "is not eligible for bonus")

#Creating Objects
Employee1 = EmployeeDetails("Yashwanth", 22, "Software Engineer", 101, 50000)
Employee2 = EmployeeDetails("Suresh", 22, "Software Engineer", 102, 4000)

# Employee1.result()
# Employee2.result()

students = [Employee1, Employee2]

for i in students:
    # print(i.name, i.age, i.Job_Role, i.Job_Id, i.salary)
    i.result()
    i.check_bonus()
