'''
Exercise 17
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH'
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), don't use lists (only strings)

'''


while True:
    s = input("Enter a string (or 'exit' to quit): ")
    if s == "exit":
        break
    reversed = ''
    for character in s:
        reversed = character + reversed
    #this can also work: reversed_s = s[::-1]

    print(reversed)

