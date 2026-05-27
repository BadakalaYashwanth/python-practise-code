# Parent Class
class Employee:

    # Method to store employee basic details
    def company(self, name):

        # Storing employee name
        self.name = name

        # Printing company information
        print("The Employee is working in the Fintech Company")


# Child Class inheriting from Employee
class Developer(Employee):

    # Method to store developer role
    def role_details(self, role):

        # Storing developer role
        self.role = role

        # Printing role information
        print(f"{self.name} is working as a {self.role}")


# Grandchild Class inheriting from Developer
class Project(Developer):

    # Method to store project details
    def project_info(self, project_type):

        # Storing project type
        self.project_type = project_type

        # Printing complete employee project details
        print(f"{self.name} is working on the {self.project_type} project")


# Creating object of Project class
dev = Project()

# Calling method from Employee class
dev.company("Yaswanth")

# Calling method from Developer class
dev.role_details("Python Developer")

# Calling method from Project class
dev.project_info("Fintech App")