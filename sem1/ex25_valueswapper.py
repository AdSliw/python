'''
Exercise 25
Your task is to swap the values of x and y.

INPUT: int
x = 3 y = 2
OUTPUT: int
x = 2 y = 3

use temporary variable, not tuple method

'''

x = input('Provide x value: ')
y = input('Provide y value: ')

print('X value: ')
print('Y value: ')

z = x
x = y
y = z

print('X value after reversing', x)
print('Y value after reversing', y)
