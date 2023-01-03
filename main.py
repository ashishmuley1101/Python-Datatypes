
# Access Python List Elements

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# access item at index 0
print(my_list[0])   # O/P : p

# access item at index 2
print(my_list[2])   # O/P : o

# access item at index 11
# print(my_list[11])   # O/P : IndexError: list index out of range

#--------Negative Indexing in Python ----------

# access item at end index  (last item)
print(my_list[-1])   # O/P : z

# access item at last 3rd index(last 3rd item)
print(my_list[-3])   # O/P : m

#---------------------------------------------

#----------------------------------- List slicing in Python ------------------------------------

# returns a list with items from index 2 to index 4 " : " is used for setting range for slicing list
print(my_list[2:5])   # O/P : ['o', ' g', 'r']

# return items from index 5 to end
print(my_list[5:])    # O/P : ['a', 'm', 'i', 'z']

# return items beginning to end
print(my_list[:])     # O/P : ['p', 'r', 'o', ' g', 'r', 'a', 'm', 'i', 'z']

# return items empty list : my_list[(start)6:5(end)] always start item is greater than end item
print(my_list[6:5])   # O/p : [] --> empty list

#-----------------------------------------------------------------------------------------------

