'''
Exercise 16

Enter any file name together with it's extension.
Check if the entered file name is of type pdf or others.
INPUT: str
Exemplary input
Enter the filname together with it's estension: ...
OUTPUT: str
Exemplary output
Your file has an extension "2s"
Program should implement error handling. In a case that a filename without an extension was entered, the following message should appear:
You entered a filename without an extension, try once more


use:
input()
string slicing
for volunteers/advanced use ternary operator

tests:
file01.docx, myBook.pdf, file02.2s
'''
# enter a filename

# find the index of "." which separates filename and it's extension

# specify the index of the first character of your extension

# write the conditional (if statement), using string slicing, substring your extension and print messages

# for advanced -> use ternary operator

# Get the file name from the user
file_name = input("Enter the file name together with its extension: ")
dot_index = file_name.find(".")
if dot_index != -1:
    extension = file_name[dot_index+1:]
    result = "Your file is of type pdf" if extension == "pdf" else "Your file is not of type pdf"
    print(f"Your file has an extension '{extension}'")
else:
    print("You entered a filename without an extension, try once more")
