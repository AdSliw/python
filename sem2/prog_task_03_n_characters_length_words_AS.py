'''
Programming Task 03 (file pt_03b.py)
Points: 15

https://www.w3schools.com/python/python_regex.asp

On the basis of Exercise 190,
Using RE, in 'shakespeare.txt' file, find and print all the 6-characters length words which starts with a vowel and ends with a consonant.
Additionally, print the amount of these words.
Vowels: 'aeoiuy'
Consonants: 'bcdfghjklmnpqrstvwz'
Think about the following Special Sequences
\b
\w
{}

Start your analysis from the line no 253.

`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.
Use input function to enter filepath

Exemplary start 
###############################################
Text analyzer - finds all 6 characters length words
which starts with a vowel and ends with a consonant

Enter the text filepath: PYTHON PROGRAMMING\shakespeare.txt
Enter the line number from which you want to start analysis: 253 

Results:
['eating' ...]
The amount of words is 275

'''
import re
import sys


def get_text(file_path: str, start_line: int) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text fileS
        start_line: text analysis should start at this specyfic line
    Returns:
        text
    '''
    with open(file_path, "r") as file:
        file_content = file.read()
        file_content_split = file_content.splitlines()[start_line:] #253
        return "".join(file_content_split)

def n_characters_length_words(textfile_path, analysis_line):
    file_content = get_text(textfile_path, analysis_line)
    word_list = re.findall(r"\b[aeoiuy]\w{4}[bcdfghjklmnpqrstvwz]\b", file_content)
    print(word_list)
    print(f"The amount of words is {len(word_list)}.")

try:
    print('''
    ###############################################
    Text analyzer - finds all 6 characters length words
    ''')
    textfile_path = input("Enter the text filepath: ") #C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\shakespeare.txt
    analysis_line = int(input('Enter the line number from which you want to start analysis:'))
    n_characters_length_words(textfile_path, analysis_line)
except FileNotFoundError:
    print("The path to the file is incorrect or the file format is not supported.")
except ValueError:
    print("Error chosing the line.")
except Exception as exception_raise:
    print("Error:" + exception_raise)

    # Your implementation

# Your code