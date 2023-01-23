'''
Exercise 30 (modify exercise 25)
Write a program that swaps the values of x and y. For this purpose create a function
swap_two_values(x:int, y:int)->None.

INPUT: int x, y
OUTPUT: int
e.g., x = 2, y = 3

use f-string, function, invoke the function with examplary data

Old program:

x = input('Provide x value: ')
y = input('Provide y value: ')

print('X value: ')
print('Y value: ')

z = x
x = y
y = z

print('X value after reversing', x)
print('Y value after reversing', y)

'''


def swap_two_values(x: int, y: int) -> None:
    x, y = y, x
    return print(f"After swapping: x = {x}, y = {y}")


x = int(input('Provide x value: '))
y = int(input('Provide y value: '))
print(f"Before swapping: x = {x}, y = {y}")
swap_two_values(x, y)

