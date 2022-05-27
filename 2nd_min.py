"""
Write Python function to find second minimum element of list.
"""
list = [0, 2, 3, 2, 5, 100]
print(list)
min1 = list[0]
min2 = list[1]
for i in range(len(list)):
    if list[i] < min1:
        min1 = list[i]
        if min1 < min2:
            min2 = min1
print(min2)

"""
second decision
"""
list = [0, 2, 3, 2, 5, 100]
list1 = set(list)
print(sorted(list1)[1])
