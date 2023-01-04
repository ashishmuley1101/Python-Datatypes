
# Python String replace() method

# The replace() method replaces each matching occurrence of a substring with another string.

text = 'bat and ball'

# replace 'ba' with 'ca'
replaced_text = text.replace('ba', 'ca')
print(replaced_text)
# Output: cat and call

# replace() Syntax : str.replace(old, new [, count])
# count (optional) - the number of times you want to replace the old substring with the new string.

song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurrences of 'let'
print(song.replace('let', "don't let", 2))

# replacing 0 occurrences of 'let'
print(song.replace('let', 'so', 0))

# Output :
# hurt, hurt heart
# Let it be, don't let it be, don't let it be, let it be
# Let it be, let it be, let it be, let it be



