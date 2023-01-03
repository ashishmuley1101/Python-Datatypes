
# Using random module and its functions over a list

import random

print(random.randrange(10, 20)) # random number between 10-20 range

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element from 0 to infinity range
print(random.random())