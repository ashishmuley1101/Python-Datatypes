
# Python String format() method

# The syntax of the format() method is: template.format(p0, p1, ..., k0=v0, k1=v1, ...)

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
# Output :
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.

# --------Simple number formatting---------

# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# Output :
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.






