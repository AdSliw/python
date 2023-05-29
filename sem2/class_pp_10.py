print('Hello world!')

import sys, re
# ----
# if re.search('[b-e]a$', sys.argv[1]):
#     print('a match' )
# else:
#     print( 'no match')
# ----
# if re.search('[a-zA-Z][aA]$', sys.argv[1]):
#     print('a match')
# else:
#     print( 'no match')
# ----
# if re.search(r"he*o", sys.argv[1]):
#     print('a match')
# else:
#     print( 'no match')
# ----
# l_txt = [
# ' hello world' ,
# ' gghello world' ,
# 'hello world and planet'
# ]

# for text in l_txt:
#     x = re.search("he.*o", text)
#     print(text + '-->' + str(x))
# ----

# The findall() function returns a list containing all matches.
# findall() function
# find list of instances: banana
import re
txt = "This is banana. Banana is very good. I like it very much.\n Here are other fruits: strawberries, raspberries, pineapples. "
# L1 = re.findall('banana', txt)
# L1 = re.findall('banana', txt.lower())
L1 = re.findall('[Bb]anana', txt)
print(L1)