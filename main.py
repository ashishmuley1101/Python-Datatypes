
# The pop() method removes the item at the given index from the list and returns the removed item.

animals1 = ['cat', 'dog', 'dog', 'pig', 'dog', 'goat', 'rabbit']

pop_element = animals1.pop(2)

print('Removed Element:', pop_element)
print('Updated List:', animals1)
# Output:
# Removed Element: dog
# Updated List: ['cat', 'dog', 'pig', 'dog']

# ----------pop() without an index, and for negative indices--------

# remove and return the last item
print('\nWhen index is not passed:')
print('Return Value:', animals1.pop())
print('Updated List:', animals1)
# O/P :
# When index is not passed:
# Return Value: rabbit
# Updated List: ['cat', 'dog', 'pig', 'dog', 'goat']

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', animals1.pop(-1))
print('Updated List:', animals1)
# O/P :
# When -1 is passed:
# Return Value: goat
# Updated List: ['cat', 'dog', 'pig', 'dog']

# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', animals1.pop(-3))
print('Updated List:', animals1)
# O/P :
# When -3 is passed:
# Return Value: dog
# Updated List: ['cat', 'pig', 'dog']






