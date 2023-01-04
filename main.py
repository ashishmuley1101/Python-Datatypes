
# Python String find() method

# The find() method returns the index of first occurrence of the substring (if found).
# If not found, it returns -1.

message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))
# Output: 12

# The syntax of the find() method is: str.find(sub[, start[, end]] )

# -------------find() With No start and end Argument-----------------

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

# Output :
# Substring 'let it': 11
# Substring 'small ': -1
# Contains substring 'be,'

# -------------find() With start and end Arguments-------------------

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))  # O/P : -1

# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))   # O/P : 3

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))  # O/P : -1

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))    # O/P : 9



