'''
Exercise 120, file pp_120.py
Write a function that will check if a word/sentence is a palindrome or not.
Use recursive implementation
These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a
'''

"https://www.dictionary.com/e/palindromic-word/"


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    import string
    # remove punctuations from text
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    # remove spaces if remove_space is True
    if remove_space:
        text = text.replace(' ', '')
    return text


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is a palindrome

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    # base case
    if len(text) <= 1:
        return True
    # recursive case
    if text[0].lower() == text[-1].lower():
        return is_palindrome(text[1:-1])
    else:
        return False


def print_palindrome_check(text: str) -> None:
    '''
    Function prints the message if text is palindrome or not

    Parameters:
        text: any text
    '''
    text = remove_punctuation(text, True)
    if is_palindrome(text):
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not a palindrome.")

print_palindrome_check("Dad") # output: Dad is a palindrome.
print_palindrome_check("Evil olive.") # output: evilolive is a palindrome.
print_palindrome_check("Never odd or even.") # output: neveroddoreven is a palindrome.
print_palindrome_check("Amore, Roma.") # output: amoreroma is a palindrome.
print_palindrome_check("test") # output: test is not a palindrome.
print_palindrome_check("ad") # output: ad is a palindrome.
print_palindrome_check("a") # output: a is a palindrome.


'''

Exercise 90, file pp_90.py
Write a program that will check if a word/sentence is a palindrome or not.
Remove punctuations and spaces
Use iterative way (loop) to check if palindrome

These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a

'''

# from string import punctuation as punct

# def is_palindrome(text: str) -> bool:
   
#    '''
#    Function checks if any text is palindrome or not

#    Parameters:
#    text: any text
#    Returns:
#    True: if text is palindrome
#    False: if text is not a palindrome
#    '''
# # your code below
#    n = ''
#    text = text.replace(' ','').lower()
#    text = ''.join(char for char in text if char not in punct)
#    for w in text:
#       n = w + n
#    if n == text:
#       return True
#    else:
#       return False
      

# print(is_palindrome('dad'))
# print(is_palindrome('mama'))
# print(is_palindrome('Evil olive'))
# print(is_palindrome('test'))
# print(is_palindrome('Never odd or even'))
# print(is_palindrome('Amore, Roma'))

