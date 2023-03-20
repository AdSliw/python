'''
Programming task 01, file pt_01.py, 20 min.
Grade : 5 points

Write a program that will remove punctuation from any string, optionally it should remove spaces.
Implement the function definition

Expected exemplary result:
Here is a text without punctuations: 'Wow Thats amazing How did you do it Im so impressed Youre awesome brilliant and talented Congratulations Well done Bravo'

Send to Teams !!!
'''


sample_text = "Wow! That's amazing. How did you do it? I'm so impressed. You're awesome, brilliant, and talented. Congratulations! Well done. Bravo!"


def remove_punctuation(text: str, remove_space: bool = True) -> str:
   '''
   Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

   Parameters:
      text: any text
      remove_space: if True, spaces are removed, if False, spaces are not removed
   Returns:
      text without punctuation, optionally spaces.
   '''
   import string
   punct = string.punctuation
   wordNoPunctuation = "".join(char for char in text if char not in punct)
   if remove_space:
      wordNoPunctuation = wordNoPunctuation.replace(' ','')
   return wordNoPunctuation


print(remove_punctuation(sample_text))