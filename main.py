
# The remove() method removes the first matching element (which is passed as an argument) from the list

# animals list
animals = ['cat', 'dog', 'rabbit', 'pig']

# 'rabbit' is removed
animals.remove('rabbit')


# Updated animals List
print('Updated animals list: ', animals)
# O/P : Updated animals list:  ['cat', 'dog', 'guinea pig']

# list contains duplicate elements, the remove() method only removes the first matching element
animals1 = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals1.remove('dog')


# Updated animals list
print('Updated animals1 list: ', animals1)
# O/P : Updated animals1 list:  ['cat', 'dog', 'guinea pig', 'dog']





