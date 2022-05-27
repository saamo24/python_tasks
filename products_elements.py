"""
Given an array. Create the array which elements are products between two neighbors.
"""
list = [0, 2, 3, 2, 5, 100]
list1 = []
for i in range(len(list)):
    c = list[i] * list[i-1]
    print(c)
