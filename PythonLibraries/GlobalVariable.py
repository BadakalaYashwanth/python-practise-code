# Global variable
# This variable is created outside the function
# So it can be accessed anywhere in the program

company = "Google"


# Function definition
def show_company():

    # Print message
    print("\nInside Function:\n")


    # Accessing global variable inside function
    print(company)


# Function call
# Executes the function

show_company()


# Print message outside function
print("\nOutside Function:\n")


# Accessing global variable outside function
print(company)