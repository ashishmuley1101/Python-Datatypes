
# The reverse() method reverses the elements of the list.

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

print("Before reverse:",prime_numbers)
# O/P : Before reverse: [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()

print('Reversed List:', prime_numbers)
# Output: Reversed List: [7, 5, 3, 2]

# -------Reverse a List Using Slicing Operator--------------------

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list
# ***** Syntax: reversed_list = systems[start:stop:step] ******
reversed_list = systems[::-1] # :-1 is the index

# updated list
print('Updated List:', reversed_list)

# O/P :
# Original List: ['Windows', 'macOS', 'Linux']
# Updated List: ['Linux', 'macOS', 'Windows']





