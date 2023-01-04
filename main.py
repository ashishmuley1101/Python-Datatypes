
# accessing tuple elements using count()

letters = ('a', 'p', 'p', 'l', 'e', 1, 2, 3, 2, 9, 1, 7, 2)

print("Count : ", letters.count('l'))
print("Count : ", letters.count(2))
print("Count : ", letters.count('p'))

# Output :
# Count :  1
# Count :  3
# Count :  2

# iterating through for loop the tuple
for x in letters:
    print(x)

# Check if an Item Exists in Tuple return boolean value
print('b' in letters)    # O/p : False
print(2 in letters)      # O/p : True


