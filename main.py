
# Python String split() method

# The split() method breaks up a string at the specified separator and returns a list of strings.
# The syntax of split() is: str.split(separator, maxsplit)
# separator (optional)- Delimiter at which splits occur. If not provided, the string is splitted at whitespaces.
# maxsplit (optional) - Maximum number of splits. If not provided, there is no limit on the number of splits.

text = 'Python is a fun programming language'

# split the text from space
print(text.split(' '))
# Output: ['Python', 'is', 'a', 'fun', 'programming', 'language']

text1 = 'Love thy neighbor'

# splits at space
print(text1.split())  # O/p : ['Love', 'thy', 'neighbor']

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))  # O/p : ['Milk', 'Chicken', 'Bread']

# Splits at ':'
print(grocery.split(':'))  # O/p : ['Milk, Chicken, Bread']


# ---------split() works when maxsplit is specified----------------

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))  # O/p : ['Milk', 'Chicken', 'Bread, Butter']

# maxsplit: 1
print(grocery.split(', ', 1))  # O/p : ['Milk', 'Chicken, Bread, Butter']

# maxsplit: 5
print(grocery.split(', ', 5))  # O/p : ['Milk', 'Chicken', 'Bread', 'Butter']

# maxsplit: 0
print(grocery.split(', ', 0))  # O/p : ['Milk, Chicken, Bread, Butter']








