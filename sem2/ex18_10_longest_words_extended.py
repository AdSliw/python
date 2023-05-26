'''
Exercise 180, pp_180.py

Modify the exercise 170 - you still print to the terminal the list of the 10  the longest words in the given text, you still  have to implement 
a function get_text(). 
But additionally, text analysis should start at specyfic line. 
Implement the possibility to decide if text should be analysed without or with punctuation and from which line number the analysis should start. Pass these arguments from command line.

On the beginning of the program a message should appear.

e.g. without punctuation removal
    ###############################################
    Text analyzer - finds 10 the longest words
    Do you want to analyse text as it is or you want to remove punctuation before?
    Press 1 if text as it is
    Press 2 if program should firstly remove punctuation
    ###############################################


-->  1
The longest word in the file 'shakespeare.txt' is 'swart-complexioned' with the length of 18 characters

The longest word in the file 'shakespeare.txt' is 'Lieutenant-General' with the length of 18 characters

The longest word in the file 'shakespeare.txt' is 'Lieutenant-General' with the length of 18 characters

use map function together with lambda, readline() method

Exception handling should be implemented.
Implement the possibility of entering "file_path" and "start_line"  from command line
'''
from string import punctuation
import sys
import msvcrt

def get_text(file_path: str, start_line_choice: int = 0) -> list:

    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text fileS
        start_line: text analysis should start at this specyfic line
    Returns:
        text
    '''

    with open(file_path, 'r') as file:
        file_content = file.read().splitlines()[start_line_choice:]
        print(type(file_content))
        return file_content

def remove_punctuation(text: list, remove_punctuation_choice: bool, remove_spaces_choice: bool) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces.
    '''
    space = ' '
    if remove_punctuation_choice and remove_spaces_choice:
        text_wo_punct =  (''.join(char for char in item if char not in punctuation) for item in text)
        text_wo_spaces_and_punct =  (''.join(char for char in item if char not in space) for item in text_wo_punct)
        return text_wo_spaces_and_punct
    if remove_punctuation_choice and remove_spaces_choice == False:
        return(''.join(char for char in item if char not in punctuation) for item in text)
    if remove_punctuation_choice == False and remove_spaces_choice:
        return(''.join(char for char in item if char not in space) for item in text)
    return text

def map_longest(text: list) -> list[tuple[str, int]]:

    '''
    Function returns the list of tuples containing the words and it's length

    Parameters:
        text: any text

    Returns:
        list of tuples containing the words and it's length
    '''
    
    words_sorted = list(map(lambda item: max(item.split(), key=len) if item.strip() else '', text))
    
    words_with_len = []
    for word in words_sorted:
        temp = (word, len(word))
        words_with_len.append(temp)
    return words_with_len


def print_word_length_list(path, word_l: list[tuple[str, int]], amount_of_lines_choice: int) -> None:

    '''
    Function prints the list of tuples. Each tuple consists of word and its length

    Parameters:
        word_l: list of tuples (word, length)
        number: the amount of words to be printed
    '''

    print(f'\nThe longest words in the file:\n{path} are:\n---')
    for item in word_l[:amount_of_lines_choice]:
        string_value, int_value = item
        print(f'"{string_value}" with the length of: {int_value}\n---')

try:
    print('''
    ###############################################
    Text analyzer - finds any amount of longest 
        words you'd like from where you'd like.
    ###############################################
    ''')
    if len(sys.argv)<2:
        # file_path = r"C:\Users\Adam\Desktop\shakespeare.txt"
        file_path = input(f'Provide a path to the file: ')
    else:
        file_path = sys.argv[1]
    if 2>=len(sys.argv)<3:
        start_line_choice = int(input(f'From which line to start from?'))
    else:
        start_line_choice = int(sys.argv[2])

    amount_of_lines_choice = int(input(f'Choose the amout of lines to print: '))

    print(f'\nPress "1" to remove punctuation. \nPress anything else to skip this option.')
    remove_punctuation_choice = True if msvcrt.getwch() == '1' else False

    print(f'\nPress "1" to remove spaces \nPress anything else to skip this option.')
    remove_spaces_choice = True if msvcrt.getwch() == '1' else False


    analyzed_text = get_text(file_path, start_line_choice)
    analyzed_text_wo_punct = remove_punctuation(analyzed_text, remove_punctuation_choice, remove_spaces_choice)
    longest_words_text_wo_punct = map_longest(analyzed_text_wo_punct)
    print_word_length_list(file_path, longest_words_text_wo_punct, amount_of_lines_choice)

except FileNotFoundError:
    print('File not found!')
except ValueError:
    print('Error choosing the line!')
except Exception as exception_raise:
    print('Error: ' + str(exception_raise))

