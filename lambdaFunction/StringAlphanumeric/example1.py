import re

# String with letters and numbers
text_normal = "abc123"
text_special= "abc1233#%^&*()"


# Regex pattern
# ^ = Start of string
# [a-zA-Z0-9]+ = One or more alphabets or numbers
# $ = End of string

result_normal = re.match("^[a-zA-Z0-9]+$", text_normal)
result_special = re.match("^[a-zA-Z0-9]+$", text_special)

if result_normal:
    print(f"\n{text_normal}: Valid")
else:
    print(f"\n{text_normal}: Invalid")


if result_special:
    print(f"\n{text_special}: Valid")
else:
    print(f"\n{text_special}: Invalid")