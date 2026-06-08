def uni(arr):

    # Loop through each element in the array
    for i in range(len(arr)):

        # Compare the current element with all elements after it
        for j in range(i + 1, len(arr)):

            # Check if the current element matches any other element
            if arr[i] == arr[j]:

                # Duplicate found, so return a message
                return "The array contains duplicates"

    # No duplicates were found after checking all elements
    return "All numbers are unique"


# Input array
arr = [1, 2, 3, 3, 5, 6, 7, 8, 9, 0]

# Call the function and print the result
print("Result:", uni(arr))