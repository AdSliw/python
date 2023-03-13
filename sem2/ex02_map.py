'''
Exercise 20, file pp_20.py
Write a program that will raise all the elements of a given list to the third power
Input : list of integers
e.g., num = [1, 2, 3, 4, 5]
Returns : list of integer numbers raised to the third power

use map function
'''

num = [1, 2, 3, 4, 5]

result = map(lambda x: x * x, num)
print(list(result))