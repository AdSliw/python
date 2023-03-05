'''
Exercise 18
Write a program that prints first 10 primes, separated by a comma.
(Use a while loop and a break statement in your solution.)
INPUT: prime_count = 10
OUTPUT: str. e.g., 2,3,5,7,11,13,17,19,23,29
Hint: what is a prime numer
https://thirdspacelearning.com/blog/what-is-a-prime-number/

First think about how to implement if the number is prime
'''

n = int(input("Enter the number of primes you want to print: "))

num = 2
count = 0
while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        if count == 0:
            print(num, end='')
        else:
            print(',', num, end='')
        count += 1
    num += 1
