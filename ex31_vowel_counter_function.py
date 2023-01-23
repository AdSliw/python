'''
Exercise 31 (modify exercise 15)
Write a program that counts vowels in a string
The program should implement the possibility for the user to enter any word.

INPUT: str
OUTPUT: str

DEFINE YOUR OWN FUNCTION:
    count_vowels(text:str)->int
    remember about docstring

Finally
use input() function to enter text
invoke count_vowels function
use f-string formatting together with print function

vowels = 'aeiou'

The exemplary input:
Enter a word ...

The exemplary output in  terminal should be:
You have 6 vowels in the word "Appalachicola"
Tests:
VOWELS -> 2 vowels
vowels -> 2 vowels
Appalachicola -> 6 vowels

'''


def count_vowels(text: str) -> int:
    char_count = 0
    vowels = 'aeiouAEIOU'
    for char in text:
        if char in vowels:
            char_count = char_count + 1
    return char_count

text = input("Enter a word... ")
vowel_count = count_vowels(text)
print(f"You have {vowel_count} vowels in the word {text}")

