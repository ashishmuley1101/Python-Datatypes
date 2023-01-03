
# Conversion numbers data type in Python

#   implicit conversion (automatically by interpreter)--------------------

num1 = 5 # int data type
num2 = 2.5 # float data types
num3 = num1 + num2 # float data types ---> implicit conversion (automatically by interpreter)
print(num3, 'is of type', type(num3)) # type() return float data type

# -----------------------------------------------------------------------

#--------------------------------explicit conversion -------------------

num4 = 5.42 # float data types
num5 = int(num4) # int data types ---> explicit conversion(Type caste)
print(num5, 'is of type', type(num5)) # type() return int data type

num6 = '8+2j' # string data types
num7 = complex(num6) # complex data types ---> explicit conversion(Type caste)
print(num7, 'is of type', type(num7)) # type() return complex data type
