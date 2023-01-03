
# The copy() method returns a shallow copy of the list.

# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()

print('Copied List:', numbers)
# Output: Copied List: [2, 3, 5]

# ---------shallow copy using the slicing syntax-----------
# copy() in new list not changing old list

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)
# Output :
# Old List: ['cat', 0, 6.7]
# New List: ['cat', 0, 6.7, 'dog']






