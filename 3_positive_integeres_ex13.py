# '''
# Exercise 13
# Write a program, your task is to enter 3 positive integers x, y, z, calculate and print the least number among them
# Use input() function and conditionals.
# INPUT: int
# OUTPUT: int
# '''

number1 = int(input('Enter the first integer number: '))
number2 = int(input('Enter the second integer number: '))
number3 = int(input('Enter the third integer number: '))

if number1 and number2 and number3 > 0:
    if number1 > number2:
        if number1 > number3:
            print(number1)
    elif number2 > number3:
        if number2 > number1:
            print(number2)
    elif number3 > number1:
        if number3 > number2:
            print(number3)
else:
    print('Error!')



