from string import punctuation
import sys

def get_text(file_path: str, start_line_choice: int = 0) -> str:

    with open(file_path, 'r') as file:
        file_content = file.read().splitlines()[start_line_choice:]
        return file_content

def remove_punctuation(text: list, remove_punctuation_choice: bool = False, remove_spaces_choice: bool = False) -> list:

    space = ' '
    if remove_punctuation_choice and remove_spaces_choice:
        text_wo_punct =  (''.join(char for char in item if char not in punctuation) for item in text)
        text_wo_spaces_and_punct =  (''.join(char for char in item if char not in space) for item in text_wo_punct)
        return text_wo_spaces_and_punct
    if remove_punctuation_choice == True and remove_spaces_choice == False:
        return(''.join(char for char in item if char not in punctuation) for item in text)
    if remove_punctuation_choice == False and remove_spaces_choice == True:
        return(''.join(char for char in item if char not in space) for item in text)
    return text

def map_longest(text: list) -> list[tuple[str, int]]:

    words_sorted = list(map(lambda item: max(item.split(), key=len) if item.strip() else '', text))
    
    words_with_len = []
    for word in words_sorted:
        temp = (word, len(word))
        words_with_len.append(temp)
    return words_with_len


def print_word_length_list(path, word_l: list[tuple[str, int]], amount_of_lines_choice: int) -> None:

    print(f'\nThe longest words in the file:\n{path} are:\n---')
    for item in word_l[:amount_of_lines_choice]:
        string_value, int_value = item
        print(f'"{string_value}" with the length of: {int_value}\n---')

if len(sys.argv)<2:
    file_path = r"C:\Users\Adam\Desktop\shakespeare.txt"
else:
    file_path = sys.argv[1]
if 2>=len(sys.argv)<3:
    start_line_choice = 0
else:
    start_line_choice = int(sys.argv[2])

amount_of_lines_choice = 30
remove_punctuation_choice = input('Remove punctuation y/n?')
remove_spaces_choice = input('Remove spaces y/n?')


analyzed_text = get_text(file_path, start_line_choice)
analyzed_text_wo_punct = remove_punctuation(analyzed_text, remove_punctuation_choice, remove_spaces_choice)
longest_words_text_wo_punct = map_longest(analyzed_text_wo_punct)
print_word_length_list(file_path, longest_words_text_wo_punct, amount_of_lines_choice)
