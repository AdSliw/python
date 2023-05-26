'''
Exercise 170, pp_170.py

Modify the exercise 160 - print to the terminal the list of the 10  the longest words in the given text,  you still have to implement 
a function get_text() to get text from file. 

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters
The longest word in the file 'shakespeare.txt' is '726002026compuservecom' with the length of 22 characters

Use map function together with lambda

Exception handling should be implemented.

Implement the possibility of entering file_path from command line
'''

from string import punctuation
import sys

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
    # other way: text_wo_punct = "".join(character for character in text if character not in punct)
    text_wo_punct = ''
    for string_element in text:
        if string_element not in punctuation:
            text_wo_punct += string_element
    return text_wo_punct

def map_longest(text: str, fast_mode: str, number: int) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        list of touples with word and its length
    '''
    words_with_len = []
    if fast_mode == str('1'):
        print('Fast mode initiated.')
        words_sorted = sorted(text.split(), key=len, reverse=True)
        for word in words_sorted:
            temp = (word, len(word))
            words_with_len.append(temp)      
    else:
        print('Slow mode initiated.')
        words = text.split() #list
        longest_words = []
        for i in range(number):
            a = max(words, key=lambda word: len(word))
            longest_words.append(a)
            words.remove(a)
        for element in longest_words:
            words_with_len.append([element, len(element)])
    return words_with_len


def print_results(path, word_l: list[tuple[str, int]], number: int) -> None:
    '''
    Function prints the list of tuples. Each tuple consists of word and its length

    Parameters:
        word_l: list of tuples (word, length)
        number: the amount of words to be printed

    !!! Print to the terminal the list of the 10  the longest words in the given text !!!
        
    '''
    print(f'\nThe longest words in the file:\n{path} are:\n---')
    for item in word_l[:number]:
        string_value, int_value = item
        print(f'"{string_value}" with the length of: {int_value}\n---')

try:
    fast_mode = input(f'To use fast mode: input "1", to use lambda: input anything else.\n')
    if fast_mode == str('1') and len(sys.argv)<2:
        file_path = input('Provide a path to the file: ')
        number = int(input(f'\nChoose the amout of lines to print: '))
        print_results(file_path, map_longest(remove_punctuation(get_text(file_path)),fast_mode, number), number)
    elif len(sys.argv)<2:
        file_path = input('Provide a path to the file: ')
        number = int(input(f'\nChoose the amout of lines to print: '))
        print_results(file_path, map_longest(remove_punctuation(get_text(file_path)),fast_mode, number), number)
    else:
        number = int(input(f'\nChoose the amout of lines to print: '))
        print_results(sys.argv[1], map_longest(remove_punctuation(get_text(sys.argv[1])),fast_mode, number), number)
except FileNotFoundError:
    print('File not found!')
except ValueError:
    print('Error choosing the line!')
except Exception as exception_raise:
    print('Error: ' + str(exception_raise))

#  file_path = r"C:\Users\Adam\Desktop\shakespeare.txt"