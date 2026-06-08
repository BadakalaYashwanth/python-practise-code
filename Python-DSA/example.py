# Function that accepts a variable number of arguments
# *args collects all passed values into a tuple
def display(*args):

    # Loop through each argument received
    for value in args:

        # Print the current argument
        print(value)

# Function call with one argument
display(1)

# Function call with three arguments
display(20, 1, 6)