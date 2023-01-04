
# Access String datatype in Python

greet = 'hello'

# access 1st index element
print(greet[1])   # O/p : e

# ------Negative Indexing-----

# access 4th last element
print(greet[-2])  # O/p : l

# Access a range of characters in a string by using the slicing " : "

# access character from 1st index to 3rd index
print(greet[1:4])  # O/p : ell

# strings are immutable. That means the characters of a string cannot be changed

message = 'Hello'
# message[0] = 'Y'
# print(message) # Error...! --> TypeError: 'str' object does not support item assignment

# Assign the variable name(message) to a new string name variable

message = 'Hello Friends'

# assign new string to message variable
message = 'How are you ?'

print(message)   # O/p :  Hello Friends

#-------- Python Multiline String ----------

# multiline string using  -- """ text """ ---

message = """
Never gonna give you up
Never gonna let you down
"""

print(message)


