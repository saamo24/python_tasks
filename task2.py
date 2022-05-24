"""
2․ Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""


temp = int(input("Input a temperature in Celsius: "))
for i in range(temp):
    i = temp + 32
print(f"Temperatue in Farenheit is {i}")

