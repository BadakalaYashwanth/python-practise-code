# Import random module
import random


# random.randrange(start, stop, step)

# start = starting number
# stop  = ending number (excluded)
# step  = jump value


number = random.randrange(5, 100, 2)


"""
| Part | Meaning         |
| ---- | --------------- |
| 5    | Start from 5    |
| 100  | Stop before 100 |
| 2    | Jump by 2       |

"""

# Print random number
print("\nRandom Number:\n")

print(number)