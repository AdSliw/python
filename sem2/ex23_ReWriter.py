'''
Exercise 230 (file pp_230.py)
Create a class that will be responsible for reading text from file and writting text to file

Class data attributes:
filepath: str, file path of the file
start_line: int, the line number from which you start reading the file
_text:str, text that was read from file

Implement class procedural attributes:
def __init__(self, filepath, startline=0):
def get_text(self) -> str:
def read_from_file(self) -> None:
def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:

Exception handling should be implemented

Enter filepath to read from file and startline using input() function
'''


class ReWriter:
    def __init__(self, filepath, start_line=0):
        self.filepath = filepath
        self.start_line = start_line
        self.read_text = ''

    def read_from_file(self) -> None:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                self.read_text = ''.join(lines[self.start_line:])
        except Exception as e:
            print('Reading error:', str(e))

    def get_text(self):
        self.read_from_file()
        return self.read_text

    def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:
        try:
            new_filepath = f_path.replace('.txt', '_new.txt')
            with open(new_filepath, mode, encoding='utf-8') as to_file:
                to_file.write(text)
        except Exception as e:
            print('Writing error:', str(e))

path_to_the_file = input('Provide a filepath: ')
line_to_start_writing = int(input('Provide a starting line: '))
new_text = ReWriter(path_to_the_file, line_to_start_writing)
new_text.read_from_file()
new_text.write_to_file(new_text.read_text, new_text.filepath)

