
# Python list extend() method

# extend() joining two list in single list
# add items of a list (rather than the list itself) to another list, use the extend() method.

# ------------------append() adding two list------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("Before append = ", list1)  # O/P : Before append =  [1, 2, 3]

list1.append(list2)

print("After append = ", list1)  # O/P : After append =  [1, 2, 3, [4, 5, 6]]

#-------------------------------------------------------------------------------

# To overcome the append() adding two list we use extends()

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("Before extend = ", list1)  # O/P : Before append =  [1, 2, 3]

list1.extend(list2)

print("After extend = ", list1)  # O/P : After append =  [1, 2, 3, 4, 5, 6]







