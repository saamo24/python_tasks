"""
Write a program in Python to remove duplicate items from a list.
"""

list = [1, 2, 2, 5, 5, "aaa", "aAa", "aaa"]

for i in list:
    for j in list:
        if i == j:
            list.remove(i)
print(list)

#with sed
list = [1, 2, 2, 5, 5, "aaa", "aAa", "aaa"]
list1 = set(list)
print(list1)

