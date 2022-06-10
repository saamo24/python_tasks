'''
#1
import sys
arguments = sys.argv
print("qanak", len(sys.argv))
'''
'''
#2
import sys
arguments = sys.argv
list1 = (f"{arguments}")  #arg1 arg2 arg3
print (list1)
'''
'''
# 3
import sys
arguments = sys.argv
str = (f"{arguments[1]}, {arguments[2]}, {arguments[3]}")
str1 = str.title()
print(str1)
'''
'''
#4
print("Enter Number:")
number = input()
print("Enter Letter")
letter = input()
number = int(number)
multypy = letter * number

print(multypy)
'''
# str = input("Input word: ")
# count = 0
# for letter in range(str):
#     if letter == "a":
#         continue
#     count = count + letter
#     print(count)
"""
# 6
for i in range(1, 6):
    for j in range(1,i+1):
        print('*', end=" ")
    print('\r')
"""
'''
#7
b = 0
for i in range(5, 0, -1):
    b += 1
    for j in range(1, i+1):
        print('*', end=" ")
    print('\r')
'''
'''
#8
import sys
argument = int(sys.argv[1])
argument1 = int(sys.argv[2])
#n = sys.argv
def is_prime(argument):
    for i in range(2, int(argument**0.5)):
        if argument % i == 0:
           return "number is prime"
        else:
            return "numper is NOT prime"
print(is_prime(argument))
print(is_prime(argument1))
'''
'''
#9, 10
x = int(input('Input first num: '))
y = int(input('Input second num: '))
def pqyndbaz(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
    return pqyndbaz(y, x % y)
print(f'Amenapoqr Yndanur bazmapatik = {pqyndbaz(x, y)}')


#  Implement function to return ամենամեծ ընդհանուր բաժանարար

def lcm(x, y):
        
    return int(f'Amenamec yndhanur bajanarar {x*y/pqyndbaz(x, y)}')

print(lcm(x, y))
'''
'''
#11
num = int(input("Input number: "))
num1 = int(input("Input power: "))

power = lambda num, num1: num ** num1
print(f'The power is equal {power(num, num1)}')
'''
'''
#12
name = lambda fname, lname: f"Full name is: {fname} {lname}"
print(name("Samvel", "Abrahamyan"))
'''
'''
#13
print((lambda x, y: x**y)(5, 3))
'''
'''
#14
number = int(input("Please input a number: "))
count = 0
for i in range(1, number+1):
    count += i
print(count)
'''
'''
#15
num = int(input("Nermucel tivy: "))
def fibo(n):
    if num < 0:
       return "ERROR"
    a = 0
    b = 1
    if num == 1:
        return 1
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
    return b
print(fibo(num))
'''
'''
#16
def fact():
    fact = 1
    i = int(input("NERMUCEL TIVY: "))
    if i < 0:
        print("!!!!!ERRRROOOORRRR!!!!!")
    else:
        while (i > 0):
            fact *= i
            i = i - 1
        print(f'Factorialy havasare {fact}')
fact()
'''
'''
#17
tiv = int(input("Nermuceq tivy: "))
count = 0
for i in range(1, tiv+1):
    count+=i
print(f'1 - {tiv} gumary havasar e {count}')
'''
'''
#18
print(sum(int(i) for i in str(input("input number "))))
'''
'''
#19
tiv = int(input("Enter a number: "))
numb = tiv
rev = 0
while(tiv>0):
    dig = tiv % 10
    rev = rev * 10 + dig
    tiv = tiv // 10
if(numb == rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
'''
'''
#21
def binary(num):
    if (num > 0):
        binary((int)(num / 2))
    print(num % 2, end= '')

num = int(input("Enter a decimal number: "))
binary(num)
'''
'''
#22
list = list(input("input "))
z = 0
for i in range(len(list)):
    c = pow(2, i)
    z += c
print(z)
'''
#20
#23
#24

'''
#25
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in weekdays:
    if len(day) == 6:
        print(day)

days = filter(lambda day: day if len(day) == 6 else '', weekdays)
'''
'''
#26
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1, list2)
list3 = map(lambda x, y: x + y, list1, list2)

print(list(list3))
'''
