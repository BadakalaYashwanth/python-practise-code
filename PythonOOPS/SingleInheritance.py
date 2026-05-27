class Employee:
    # Method to store employee details
    def company(self, name, role, project_type):
        self.name = name
        self.role = role
        self.project_type = project_type

        # Printing company information
        print("The Employee are working in the Fintech Company")

class Developer(Employee):

    # Method to display developer working details
    def programming(self):
        
        # Printing employee role and project details
        print(f'Here {self.name} is working as {self.role} in the {self.project_type}')

# Creating object of Developer class
dev = Developer()

# Calling company method and passing employee details
dev.company("Yashwanth", "Software Developer", "Payment Gateway")

# Calling programming method
dev.programming()