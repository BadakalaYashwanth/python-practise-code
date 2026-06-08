# Solve a system of two linear equations:
#
# ax + by = c
# mx + ny = o
#
# using Cramer's Rule to find the values of x and y

def equation(a, b, c, m, n, o):

    # Calculate the determinant of the coefficient matrix
    temp = a * n - b * m

    # Check if a unique solution exists
    if temp != 0:

        # Calculate the value of x using Cramer's Rule
        x = (c * n - b * o) / temp

        # Calculate the value of y using Cramer's Rule
        y = (a * o - m * c) / temp

        # Display the values of x and y
        print("x =", x)
        print("y =", y)

    else:

        # Determinant is zero, so no unique solution exists
        print("No unique solution exists")


# Coefficients of the equations
a, b, c = 5, 9, 4
m, n, o = 7, 9, 4

# Call the function to solve the equations
equation(a, b, c, m, n, o)