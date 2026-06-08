# Function to add two numbers without using the '+' operator
# Uses bitwise operations to calculate the sum
def add_sum(num1, num2):

    # Continue until there is no carry left
    while num2 != 0:

        # Find the carry bits using bitwise AND
        data = num1 & num2

        # Add the numbers without considering carries using XOR
        num1 = num1 ^ num2

        # Shift the carry bits left by one position
        # so they can be added in the next iteration
        num2 = data << 1

    # Return the final sum
    return num1


# Call the function and print the result
print(add_sum(2, 19))