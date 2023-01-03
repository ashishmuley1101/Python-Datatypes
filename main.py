
# The index() method returns the index of the specified element in the list

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # O/P : 1

print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)    # O/P : 6

print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # O/P : Error!

# 'i' between 3rd and 7th index is searched
index = alphabets.index('i', 3, 7)

print('The index of i:', index)   # O/P : 6







