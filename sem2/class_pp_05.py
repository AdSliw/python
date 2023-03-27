# DAC Algorithm - Beaks the problem to two more smaller problems

# Very slow, but simple

# iterative way
def multi_iter(a, b):
   result = 0
   while b > 0:
      result += a
      b -= 1
   return result

# recustion way

def multi_rec(a, b):
   if b == 0:
      return 0
   if b == 1:
      return a
   else:
      return a + multi_rec(a, b)
   

a = 4
b = 3
print(f'{a} * {b} = {multi_iter(a,b)}')
print(f'{a} * {b} = {multi_rec(a,b)}')

#todo: check timers for both