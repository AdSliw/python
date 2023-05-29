# infile = open('shakespeare.txt', 'r', encoding = 'utf-8')

# stuff = infile.read()
# infile.close()
# lines = stuff.split('\n')
# for line in lines:
#     print(f'{line}, : {len(line)} characters')
# ---
# infile = open('shakespeare_short.txt', 'r', encoding = 'utf-8')
# stuff = infile.readlines()
# infile.close()
# for line in stuff:
#     print(f'{line}, : {len(line)} characters')
#---
# with open('shakespeare_short.txt', 'r', encoding = 'utf-8') as infile:  
#     lines = infile.readlines()
#     for line in lines:
#         print(f'{line}, : {len(line)} characters')
#---

## 8. Writing to a file with closing files
# try:    
#     a = int(input('Enter the integer numer \'a\': ... '))
#     b = int(input('Enter the integer numer \'b\': ... '))
#     num = a / b
#     print(f'The result of division {a} / {b} = {num} ' )
#     print( 'Writting the result to the file .... ' )
#     file = open('testfile.txt', mode='a', encoding = ' utf-8 ' )
#     file.write(f'\nThe result of division {a} / {b} = {num}')
# except ValueError:
#     print('You didn\'t enter the valid number!')
# except ZeroDivisionError:
#     print('You can\'t divide by O!')
# except FileNotFoundError:
#     print("Fi1e doesn't exist")
# except :
#     print('Something went wrong!') # for all other errors
# else:
#     print('Fi1e is closed!')
# # useful for clean-up code that should be run no matter what else happened (e. g.close a file)
# finally :
#     file.close()
#---

## 9. Writing to a file without closing directly but with with
# try:
#     a = int(input('Enter the integer numer \'a\': ... '))
#     b = int(input('Enter the integer numer \'b\': ... ')) 
#     num = a / b
#     print(f'The result of division {a} / {b} = {num} ' )
#     print( 'Writting the result to the file .... ' )
#     with open('testfile.txt', 'a' , encoding= 'utf-8') as file:
#         file.write(f' \nThe result of division {a} / {b} = {num} ' )
# except ValueError:
#     print('You didn\'t enter the valid number!')
# except ZeroDivisionError:
#     print('You can\'t divide by 0!')
# except FileNotFoundError:
#     print('Fi1e doesn\'t exist')
# except :
#     print('Something went wrong!') # for all other errors
#---

# REGEXP
'''
findall(pattern, string, flags=O) - returns a list containing all matches
search(pattern, string, flags=O) - returns a Match Object if there is a match anywhere in the string
split(pattern, string, maxsplit=O, flags=O) - spljt string by the occurrences of pattern and returns the list of them
sub(pattern, repl, string, count=O, flags=O) - replaces one or many matches with a string

pattern - [mandatory] the pattern which has to be found in the string
string - [mandatory] the string in which the pattern _has to be found
repl - [mandațory] the value which has to be replaced in the string in place of matched pattern.
flag - [optional]
maxsplit- [optional] the maximum limit on number of splits
'''


# import re, sys
# if re.search('ab', sys.argv[1]): #Returns „Match object” or „None”
#     print('a match')
# else: 
#     print( 'no match')

'''
PATTERN MATCHING
• import re
• remșearch(pattecn, string) -9
returns Match obiect nr None
If we use jnsjdę if statement, a match Object will
evaluate to True and a None Object will evaluate to
False

A single symbol, for example: 'a', '3', 'k', etc. These will
match a string that consists of just the symbol indicated
A concatenation or sequence of characters. For
example: lab', '3g', 'kk', etc. Such an expression matches
if the giyentext contains them.
-9 any single character (except newline character),
'*' -9 zero more occurrenoes (charącterș) e,g., 'a*b'
'.*' -5 zero more occurrences (chąracterș), except
newline character


'''

# 3. test with c, cba, abc, abcde
# Match îf all the characters are aț the beginning.
# import re, sys
# if re.search('^abe', sys.argv[1]):  
#     print('a match')
# else:
#     print('no match')

'''
[ ] - A set of characters, match if any characters in
brackets exists in the string,
[arn] - Returns a match where one of the specified
characters (a, r, or n) are present (one is enough)
[a-n] - Returns a match for any lowevcase character,
between a and n, are present
[^arn] Returns a match for any character EXCEPT a,
r, and n
[0123] - Returns a match where any of the specified
digits (0, 1, 2, or 3) are present
[0-9] - Returns a match for any digit between 0 and 9
'''

# 4. test with cef, efg
# A set of characters, match if any characters in the brackets exists in the string
# import re, sys
# if re.search('[a-d]', sys.argv[1]):
#     print('a match')
# else:
#     print( 'no match')

