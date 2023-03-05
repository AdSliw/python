'''
Exercise 19
There is a list
hashtags = ['spring','summer','winter']
Connect these element with "#". Add this sign also at the beginning.
Print the result to the terminal
INPUT: list
OUTPUT: str
Expected result: #spring#summer#winter
'''

hashtags = ['spring','summer','winter']
result = "#"
i = 0
while i < len(hashtags):
    result += hashtags[i]
    if i != len(hashtags) - 1:
        result += "#"
    i += 1
print(result)
