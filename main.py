
# Python String encode() method

# The encode() method returns an encoded version of the given string.
# The syntax of encode() is: string.encode(encoding='UTF-8',errors='strict')
# encoding - the encoding type a string has to be encoded to
# errors - response when encoding fails.

title = 'Python Programming'

# change encoding to utf-8
print(title.encode())
# Output: b'Python Programming'

# -----Encode to Default Utf-8 Encoding---------------------

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

# Output :
# The string is: pythön!
# The encoded version is: b'pyth\xc3\xb6n!'

# ---------Encoding with error parameter------------------

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

# Output :
# The string is: pythön!
# The encoded version (with ignore) is: b'pythn!'
# The encoded version (with replace) is: b'pyth?n!'

# ignore - ignores the unencodable unicode from the result (error)
# replace - replaces the unencodable unicode to a question mark ? (error)







