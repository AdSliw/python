
















def fizz_buzz(num) -> None:
    '''
    Exercise 01, file pp_01.py
    Write a function named fizz_buzz(num) that will return the string 'Fizz' if the num parameter  is divisible by 3,
    will return the string 'Buzz' if the num is divisible by '5',
    will return the string 'FizzBuzz' if the num is divisible by 3 and 5
    will return num for any other number
    Function should include docstring
    Program should implement entering the number many times  during runtime. Typing "q"  should cause quitting the program.
    '''
    print(fizz_buzz.__doc__)

    if num == str('q') or num == '':
        return num
    num = int(num)
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

while True:
    check = fizz_buzz(input('Provide a number: '))
    if check == 'q':
        break
    else:
        print('Provide a proper value!')







