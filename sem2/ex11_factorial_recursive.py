'''
Exercise 110, file pp_110.py
Write a program that computes the value of n factorial - n!
Use RECURSIVE implementation
Expected results
-10! => ERROR
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4
10! = 3628800
32! = 263130836933693530167218012160000000
n! = 1 * 2 * 3 * .... * n

'''

negative_num_error = -9999

import time

def factorial(n):
    '''
    Functions calculates the factiorial of n

    Parameters:
        n: number, positive int
    Returns:
        The factorial or the error code

    '''
    # check if n is a negative number
    if n < 0:
        return "ERROR"
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    return n * factorial(n-1) - factorial(n-1)

for i in range(33):
    tic = time.perf_counter()
    print(str(i + 1) +'. ',factorial(i))
    toc = time.perf_counter()
    print(f"Completed in {toc - tic:0.4f} seconds\n")

toc_external = time.perf_counter()
print(f"All completed in {toc_external - tic_external:0.4f} seconds\n")