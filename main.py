
# Python String startswith() method

# The startswith() method returns True if a string starts with the
# specified prefix(string). If not, it returns False

# The syntax of startswith() is: str.startswith(prefix[, start[, end]])
# start (optional) - Beginning position where prefix is to be checked within the string.
# end (optional) - Ending position where prefix is to be checked within the string.

message = 'Python is fun'

# check if the message starts with Python
print(message.startswith('Python'))
# Output: True


# -----startswith() Without start and end Parameters---
text = "Python is easy to learn."

result = text.startswith('is easy')
print(result)   # O/p : False

result = text.startswith('Python is ')
print(result)  # O/p : True

# -----startswith() With start and end Parameters-----

text1 = "Python programming is easy."

# start parameter: 7
# 'programming is easy.' string is searched
result = text1.startswith('programming is', 7)
print(result)  # O/p : True

# start: 7, end: 18
# 'programming' string is searched
result = text1.startswith('programming is', 7, 18)
print(result)  # O/p : False

result = text1.startswith('program', 7, 18)
print(result)  # O/p : True

# ------startswith() With Tuple Prefix--------------

text3 = "programming is easy"
result = text3.startswith(('python', 'programming'))

# prints True
print(result)

result = text3.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text3.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)

# Output :





