
# In Python A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Output :
# ()
# (1, 2, 3)
# (1, 'Hello', 3.4)
# ('mouse', [8, 4, 6], (1, 2, 3))

# Creating a tuple with one element is a bit tricky and one element normal data type
# We will need a trailing comma " , " to indicate that it is a tuple.

var1 = ("hello")
print(type(var1))  # O/P :  <class 'str'>

var2 = 123
print(type(var2))  # O/P :  <class 'int'>

# Creating a tuple having one element
var3 = ("hello",)
print(type(var3))  # O/P :  <class 'tuple'>

# Parentheses is optional
var4 = "hello",
print(type(var4))  # O/P : <class 'tuple'>





