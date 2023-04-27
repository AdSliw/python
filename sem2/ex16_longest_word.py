'''
Exercise 160, pp_160.py

Task is the same as in exercise 40 - finding the longest word in the given text, but additionally you have to implement a function get_text(). 
The new function should return the text from a file, 
Write a program with a function called map_longest() that takes a text as a parameter and returns the longest word contained in that text and its length - tuple.

Result of a program should be a message 
e.g. after punctuation removal
The longest word in the file 'shakespeare.txt' is 'internethartvmdcsouiucedu' with the length of 25 characters

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters

use map function together with lambda

Exception handling should be implemented.
Implement the possibility of entering file_path from command line
'''

def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
    Returns:
        text
    '''
    with open(file_path, 'r') as file:
        return file.read()


def remove_punctuation(text: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text_wo_punct = "".join(character for character in text if character not in punct)
    # 
    # for character in text:
    #     if character not in punct:
    #         text_wo_punct+=character
    return text_wo_punct

def map_longest(text: str) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the logest word and it's length

    '''
    words = text.split()
    longest_word = max(words, key=lambda word: len(word))
    return (longest_word, len(longest_word))

def print_results(file, word, length):
    '''
    Function prints the result.
    '''
    print(f'The longest word in the file:\n  {file} is\n {word} \nwith the length of {length} characters')

try:
    # ---
    # import os 
    # script_dir: str = os.path.realpath(os.path.dirname(__file__)) - todo - using working directory directly from script 
    # --- 
    # directory = r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\shakespeare.txt'
    directory = input(r'Provide a directory: ')
    text = get_text(directory)
    text_wo_punct = remove_punctuation(text)
    print_results(directory, map_longest(text_wo_punct)[0], map_longest(text_wo_punct)[1])
except Exception as e:
    print('Error: ' + e)

# C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\shakespeare.txt