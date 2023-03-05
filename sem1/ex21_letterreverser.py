'''
Exercise 21
For any entered string. Write a program that will
reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), use lists

'''

while True:
    string = input("Enter a string (or 'exit' to exit): ")
    if string == "exit":
        break
    else:
        string_list = list(string)
        string_list.reverse()
        reversed_string = "".join(string_list)
        print(reversed_string)

