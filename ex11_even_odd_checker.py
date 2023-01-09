# '''
# Exercise 11
# Write a program that will check whether the given number is even or odd
# INPUT: int
# use input() function
# text to appear:
# 'Enter the integer number'
#
# OUTPUT: str
# 'Even'
# or
# 'Odd'
#
# '''

number = int(input('Enter the integer number: '))
if number == 0:
    print('zero')
elif number % 2 == 0:
    print('Even')
else:
    print('Odd')

