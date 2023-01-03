
# Python list append() method

# append() adding item on last index

name = ["krack", "tom", "jerry", "snappy", "richard"]

print("Before append = ", name)
# O/P : Before append =  ['krack', 'tom', 'jerry', 'snappy', 'richard']

name.append("jack")

print("After append = ", name)
# O/P : After append =  ['krack', 'tom', 'jerry', 'snappy', 'richard', 'jack']

# ------------------append() adding two list------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("Before append = ", list1)  # O/P : Before append =  [1, 2, 3]

list1.append(list2)

print("After append = ", list1)  # O/P : After append =  [1, 2, 3, [4, 5, 6]]







