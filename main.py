
# Python String endswith() method

# The endswith() method returns True if a string end with the
# specified prefix(string). If not, it returns False

# The syntax of endswith() is: str.endswith(suffix[, start[, end]])
# start (optional) - Beginning position where prefix is to be checked within the string.
# end (optional) - Ending position where prefix is to be checked within the string.

message = 'Python is fun'

# check if the message ends with fun
print(message.endswith('fun'))

# Output: True


# -----endswith() Without start and end Parameters---
text = "Python is easy to learn."

result = text.endswith('to learn')
# returns False
print(result)

result = text.endswith('to learn.')
# returns True
print(result)

result = text.endswith('Python is easy to learn.')
# returns True
print(result)

# -----endswith() With start and end Parameters-----

text1 = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text1.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text1.endswith('is', 7, 26)
# Returns False
print(result)

result = text1.endswith('easy', 7, 26)
# returns True
print(result)

# ------endswith() With Tuple Prefix--------------

text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

#prints True
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)

# prints True
print(result)






