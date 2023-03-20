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
from string import punctuation as punct

def is_palindrome(text: str) -> bool:
   
   '''
   Function checks if any text is palindrome or not

   Parameters:
   text: any text
   Returns:
   True: if text is palindrome
   False: if text is not a palindrome
   '''
# your code below
   n = ''
   text = text.replace(' ','').lower()
   text = ''.join(char for char in text if char not in punct)
   for w in text:
      n = w + n
   if n == text:
      return True
   else:
      return False
      

print(is_palindrome('dad'))
print(is_palindrome('mama'))
print(is_palindrome('Evil olive'))
print(is_palindrome('test'))
print(is_palindrome('Never odd or even'))
print(is_palindrome('Amore, Roma'))

