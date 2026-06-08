import re

def match_text(txt_data):

    # Define a regex pattern:
    # 'a' followed by 4 to 8 consecutive 'b' characters
    pattern = 'ab{4,8}'

    # Search for the pattern in the given text
    if re.search(pattern, txt_data):

        # Return this message if a match is found
        return 'Match found'

    else:

        # Return this message if no match is found
        return 'Match not found'


# Test case 1: Contains only 2 b's, so it does not match
print(match_text("abc"))

# Test case 2: Contains 'a' followed by 6 b's, so it matches
print(match_text("aabbbbbbc"))