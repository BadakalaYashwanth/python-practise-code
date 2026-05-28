# Global variable
# This variable is created outside the function
# So it can be accessed anywhere in the program

count = 10


# Function definition
def update():

    # global keyword
    # Tells Python:
    # "Use the global variable count"
    # instead of creating a new local variable

    global count


    # Updating global variable value
    count = 30


# Function call
# Executes the function

update()


# Print updated global variable
print(count)