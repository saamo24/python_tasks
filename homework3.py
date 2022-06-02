"""

Transpose of a Matrix using List Comprehension
example [[1, 2], [3,4], [5,6], [7,8]] => [[1, 3, 5, 7], [2, 4, 6, 8]]

"""

list = [[1, 2], [3, 4], [5, 6], [7, 8]]
list1 = []
list2 = []
list3 = []
def miacum():
    for i in list:
        for j in i:
            if j % 2 == 0:
                list1.append(j)
            else:
                list2.append(j)
    list3.append(list1)
    list3.append(list2)
    return list3
print(miacum())
