"""
3․ Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
"""


year = int(input("Input a dog's age in human years: "))
if  0 <= year <= 2:
    year *= 10.5
    print(f"The dog's age in dog's years is {year}")
else:
    year *= 4
    print(f"The dog's age in dog's years is {year}")

