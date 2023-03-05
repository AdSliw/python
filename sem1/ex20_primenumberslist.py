'''
Exercise 20
Modify Exercise 18 concerning prime numbers.
Implement solution based on list object.

'''
n = int(input("Enter the number of primes you want to print: "))

primes = []
num = 2
while len(primes) < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

print(primes)
