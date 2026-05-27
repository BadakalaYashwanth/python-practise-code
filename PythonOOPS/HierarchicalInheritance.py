# Parent class
class Employee:

    def company(self):

        print("\nEmployee belongs to ABC Company")


# Child class 1
class Developer(Employee):

    def check_tasks(self, tasks):

        # Loop
        for task in tasks:

            # Condition
            if task >= 5:

                print("Completed Task:", task)

            else:

                print("Pending Task:", task)


# Child class 2
class Tester(Employee):

    def check_bugs(self, bugs):

        # Loop
        for bug in bugs:

            # Condition
            if bug > 0:

                print("Bug Found:", bug)

            else:

                print("No Bugs")


# Creating objects
dev = Developer()

tester = Tester()


# Calling parent method
dev.company()

tester.company()


# Calling child methods
dev.check_tasks([2, 5, 7])

tester.check_bugs([1, 0, 3])