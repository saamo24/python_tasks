"""
Create {1:1, 2:8, 3:27, 4:64, 5:125} dictionary using comprehension
"""

n = int(input("Input range: "))
dict1 = {k:((k*k)*k) for k in range(1, n+1)}
print(dict1)

