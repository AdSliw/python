'''
Exercise 14

Enter any file name together with it's extension e.g., file01.docx, myBook.pdf
Check if the entered file name is of type pdf or others.
INPUT: str
"Enter the filname"
OUTPUT:
"Your file is of type pdf"
"Your file is not of type pdf"

use:
input()
string slicing
ternary operator

'''

file_name = input("Enter the file name: ")
result = "Your file is of type pdf" if file_name[-4:] == ".pdf" else "Your file is not of type pdf"
print(result)
