"""
Implement function which will take number and return sum of digits in number
"""

num = list(input("Input Number: "))
def sum(num):
    print(num)
    sum1 = 0
    for i in range(len(num)):
        num[i] = int(num[i])
    for elem in num:
        sum1 += elem
    return sum1
print(sum(num))
