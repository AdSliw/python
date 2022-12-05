'''
Exercise 07
Create a string made of the first, middle and last character and print it to the terminal

Expected results
text = 'abcdefg'  # expected result: adg
text = 'abcdef'  # expected result adf

Hints:
Use string indexing to get the character present at the given index
Get the index of the middle character by dividing string length by 2
Function that returns string length:
l= len(text)

'''

text = 'abcdefg'
text_length = int(len(text) / 2)

text_2 = 'abcdef'
text_length_2 = int(len(text_2) / 2)

print(text[0],(text[text_length]), (text[-1]), sep='')
print(text_2[0],(text_2[:/2]), (text_2[-1]), sep='')



