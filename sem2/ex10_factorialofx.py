'''
Exercise 100, file pp_100.py
Write a program that computes the value of n factorial - n!
Use iterative implementation
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
import time

def factorial(n: int) -> int:
   '''
   Functions calculates the factiorial of n

   Parameters:
      n: number, positive int
   Returns:
      The factorial

   '''
   outcome = 1
   if n < 0:
      print("Error.")
   elif n == 0:
      print("1")
   else:
      for i in range(1,n + 1):
         outcome = outcome*i
   return outcome

tic_external = time.perf_counter()

for i in range(33):
    tic = time.perf_counter()
    print(str(i + 1) +'. ',factorial(i))
    toc = time.perf_counter()
    print(f"Completed in {toc - tic:0.4f} seconds\n")

toc_external = time.perf_counter()
print(f"All completed in {toc_external - tic_external:0.4f} seconds\n")