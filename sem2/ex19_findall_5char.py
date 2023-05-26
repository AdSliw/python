'''
Exercise 190

https://www.w3schools.com/python/python_regex.asp

Using RE find all the 5-characters length

Think about the following Special Sequences
\b
\w
{}


`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.

'''
import re
import sys


def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text fileS
        start_line: text analysis should start at this specyfic line
    Returns:
        text
    '''
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content
    

text = get_text(r'C:\Users\Adam\Desktop\shakespeare.txt')
five_char_length = re.findall(r'\b[a-zA-Z]{5}\b', text)
print(five_char_length)
print(len(five_char_length))