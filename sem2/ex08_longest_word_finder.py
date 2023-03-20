'''
Exercise 80, file "pp_80.py"
The text is given:
shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'
Write a program that will find and print to the terminal the longest word in the text.
In order to achieve it, implement the function that will delete all '.', ',', get the list of all words,  
use dictionary comprehension to get word:length pairs and use sorted() functio.

Expected result:
The longest word is 'trenches' with the length 8 characters.

'''


def get_longest_word(text: str) -> tuple[str, int]:
    '''
    Function returns the longest word together with its length

    Parameters:
        text: any text
    Returns:

    Exemplary result:
    ('trenches',8)
    '''
    # Remove all '.', ',' from the text
    text = text.replace('.', '').replace(',', '')
    
    # Get list of all words
    words = text.split()
    
    # Use dictionary comprehension to get word:length pairs
    word_lengths = {word: len(word) for word in words}
    
    # Use sorted() function to get the word with the longest length
    longest_word = sorted(word_lengths.items(), key=lambda x: x[1], reverse=True)[0]
    
    return longest_word

shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'
longest_word = get_longest_word(shakespeare)
print(f"The longest word is '{longest_word[0]}' with the length {longest_word[1]} characters.")
