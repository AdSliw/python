'''
ITCSP, Final Programming Task, 1LMT, group 02
(30 points)

Imagine you are a young linguist researcher
Your task is to create a program that analyzes 
the frequency of words in a given text. The program should do the following:

For the given  string of text.




Create a list of all the words.
Use a loop to iterate through the text and from each word in a list and remove all punctuations.
Use a dictionary to store the frequency of each word in the text. The keys of the dictionary should be the words, and the values should be the number of times the word appears in the text.
Use another loop to iterate through the dictionary and print out first 10 words in the text and their frequency.

In order to do your task implement the functions below.

Auxiliary information
if you want to get all punctuations as a single string use the following code
import string
punct = string.punctuation


Expected result:
======================================================
Text analyzer, version 1.0.0
======================================================

1. artificial(1)
2. intelligence(2)
3. ai(9)
4. is(6)
5. a(4)
6. rapidly(2)
7. evolving(2)
8. field(2)
9. that(9)
10. involves(2)

Total of words: 231

++++++++++++++++++++++++++++++++++++++++++++++++++
Only for volunteers / advanced if you have enough time: instead of printing first 10 words with theirs frequencies, create get_sorted_dictionary() function, 
sort all the dictionary items (in a descending way) and print out the 10 MOST FREQUENT words in the text and their frequency.
++++++++++++++++++++++++++++++++++++++++++++++++++

Expected result for advanced only:
======================================================
Text analyzer, version 1.0.0
======================================================

1. and(13)
2. ai(9)
3. that(9)
4. the(8)
5. of(8)
6. to(7)
7. is(6)
8. in(5)
9. a(4)
10. development(4)

Total of words: 231

'''


# FUNCTION DEFINITIONS


def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''


def get_word_frequency_dictionary(wordList: list) -> dict:
    '''
    Function creates the dictionary of word:frequency pairs, where the frequency is the amount of the given word in the text

    Parameters: 
        wordList: list of all words in the text

    Returns:
        dictionary of word:frequency pairs

    '''


def print_dictionary(d: dict, num) -> None:
    '''
    Function prints the given dictionary to the terminal

    Parameters:
        d: dictionary 
        num: number of dictionary items to be printed

    Examplary print result:
    1. the (3)
    2. dog (2)
    3. lazy (2)
    4. quick (1)
    5. brown (1)

    '''


def print_word_number(wordList: list) -> None:
    '''
    Function prints the total number of words in the list

    Parameters:
        wordList: list of the words

    Example: 
    Total of words: 234
    '''


def get_sorted_dictionary(d: dict) -> dict:
    '''
    Function returns sorted version of the given dctionary

    Parameters:
        d: unsorted dictionary of word:frequency pairs
    Returns:
        sorted  dictionary (on descending way) - sorting on frequency

    '''


# YOUR MAIN PROGRAM
# HERE CONTINUE YOUR PROGRAM ....

import string
punct = string.punctuation

text = '''
Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as 
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a 
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, 
including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. 
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable 
of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. 
This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge 
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach 
its development and deployment with caution and responsibility.
'''

#print(text)

def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    wordLower = word.lower()
    wordNoPunctuation = "".join(char for char in wordLower if char not in punct)
    return wordNoPunctuation


def get_word_frequency_dictionary(wordList: list) -> dict:
    '''
    Function creates the dictionary of word:frequency pairs, where the frequency is the amount of the given word in the text

    Parameters: 
        wordList: list of all words in the text

    Returns:
        dictionary of word:frequency pairs

    '''
    wordList = wordList.split()
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict

def print_dictionary(d: dict, num) -> None:
    '''
    Function prints the given dictionary to the terminal

    Parameters:
        d: dictionary 
        num: number of dictionary items to be printed

    Examplary print result:
    1. the (3)
    2. dog (2)
    3. lazy (2)
    4. quick (1)
    5. brown (1)

    '''

    dictSorted = sorted(d.items(), key=lambda item: item[1], reverse=True)
    
    for i, (key, value) in enumerate(dictSorted):
        if i >= num:
            break
        print(f"{i + 1}. {key} ({value})")



def print_word_number(wordList: list) -> None:
    '''
    Function prints the total number of words in the list

    Parameters:
        wordList: list of the words

    Example: 
    Total of words: 234
    '''
    wordLower = wordList.lower() #not necessary
    wordList = wordLower.split() 
    print("Total of words:", len(wordList))


try:
    print("====================================================== Text analyzer, version 1.0.0 ======================================================")
    textNoPunct = remove_punctuation(text)
    textAsDictionary = get_word_frequency_dictionary(textNoPunct)
    printDictionary = print_dictionary(textAsDictionary, 10)
    print_word_number(textNoPunct)
except Exception as e:
    print('Error.' + str(e))
