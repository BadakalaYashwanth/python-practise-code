# Import Counter to count the occurrences of each character
import collections

# Import pprint to display the dictionary in a readable format
import pprint

# Open the text file in read mode
with open('example3.txt', 'r') as data:
    # Read the entire file content
    # Convert all characters to uppercase so that 'a' and 'A' are treated as the same character
    # Count the occurrence of every character using Counter
    count_Data = collections.Counter(data.read().upper())

    # Convert the Counter object into a neatly formatted string
    count_Value = pprint.pformat(count_Data)

# Display the count of each character
print(count_Value)