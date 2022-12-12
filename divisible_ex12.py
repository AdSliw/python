# '''
# Exercise 12
# Write a program:
# After you will enter an intger number, called x:
# If a number is divisible by 2 and divisible by 3, print "Divisible by 2 and 3".
# If a number is divisible by 2 and not by 3, print "Divisible by 2 and not by 3"
# If a number is divisible by 3 and not by 2, print "Divisible by 3 and not by 2"
# If a number is not divisible by 2 and not by 3, print "Not divisible by 2, not divisible by 3"
# Use modulo division
# Do the tests
# '''

number = int(input('Enter the integer number: '))
if number % 2 == 0 and number % 3 == 0:
    # divisible by 2 and divisible by 3
    print('Divisible by 2 and 3')

elif number % 2 == 0 and number % 3 != 0:
    # divisible by 2 and not by 3
    print('Divisible by 2 and not by 3')

elif number % 2 != 0 and number % 3 == 0:
    # divisible by 3 and not by 2
    print('Divisible by 3 and not by 2')

else:
    print('Not divisible by 3 and 2')
