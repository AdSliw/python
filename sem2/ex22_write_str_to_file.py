#On the basis of Programming Task 03, additionally implement the functionality of writting the results to the file.

'''
Exercise 30, pp_30.py
Write a program with a function called map_longest() that 
takes a text as a parameter and returns the longest word 
contained in that text and its length - tuple.

Result of a program should be a message 
e.g.,
The longest word in the text is 'decision-making.' with the length of 16 characters

use map function together with lambda, don't deal with punctuation
'''


def map_longest(text: str) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the longest word and it's length

    '''

    words = text.split()
    longest_word = max(words, key=lambda word: len(word))
    return (longest_word, len(longest_word))
    



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

longest_word = map_longest(text)

vairable = (f'The longest word in the text is {longest_word[0]} with the length of {longest_word[1]} characters.')

with open('shakespeare_new.txt', 'w') as file:
    file.write(str(vairable))