# Function to find and display all pairs in the array
# whose sum is equal to the target value
def find_pairs(arr, target):

    # Loop through each element in the array
    for i in range(len(arr)):

        # Compare the current element with all elements after it
        for j in range(i + 1, len(arr)):

            # Check if the sum of the pair equals the target value
            if arr[i] + arr[j] == target:

                # Print the pair that satisfies the condition
                print(arr[i], arr[j])


# Input array containing numbers
arr = [1, 2, 3, 4, 5]

# Target sum value to be matched
target = 5

# Call the function to find and display valid pairs
find_pairs(arr, target)