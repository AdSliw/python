"""
SUGGESTIONS

Exercise 240, file pp_240.py

Using your konowledge from previous exercises

Your task is, using python:

DONE    0. Entering text_file_path, db_file_path, start_line 

DONE     1. Create a MyDB01.db (everything using python) Create a table Alice_tb with
        columns Id integer primary key, Line text, Length integer

DONE     2. Read text data from alice.txt (use your TextIO class from your module)

DONE     3. Analize your text:
        - lines_length data structure variable
        - save your data in lines_length variable
        - write your data to DB


DONE     3. Read first 10 data rows from your database and print to the terminal

In order to do the exercise, implement the following functions:

def get_lines_length(text: str) -> list[tuple[str, int]]:
def write_alice_tb(db_file_path: str, data: list[tuple[str, int]]) -> None:
def read_alice_tb(db_file_path: str) -> list[tuple[int, str, int]]:
def print_alice_tb(data: list[tuple[int, str, int]], number: int) -> None:

"""


import sqlite3, os, re

class LineReader:
    def __init__(self, 
                 text_file_path: str = '', 
                 db_file_path: str = '', 
                 start_line: int = 0,
                 end_line: int = -1,
                 number_to_print: int = 0
                 ) -> None:
        
        #Mains:
        self.db_file_path: str = db_file_path
        self.text_file_path: str = text_file_path
        self.start_line: int = start_line
        self.end_line: int = end_line
        self.number_to_print: int = number_to_print
        #Helpers:
        self.result_range: tuple[int, int] = (0, 3)
        self.lines_length_list: list[tuple[str, int]] = []
        self.text: list[str] = []
        self.file_name: str = ''
        self.data: list[tuple[str, int]] = []
        self.script_directory: str = ''
        self.database_values: list[tuple[int, str, int]] = []
        

    debugger = True


    def debugger(func): #this function helps in debugging - prints what the functions are outputting
            try:
                def wrapper(self, *args, **kwargs): 
                    print(f"\nStarted {func.__name__}!")
                    result = func(self, *args, **kwargs)
                    try:
                        if len(str(result)) > 32: #32 because why not
                            part_of_outcome = result[self.result_range[0]:self.result_range[1]]
                        else: 
                            part_of_outcome = result
                        print(f"Part of outcome: {part_of_outcome}")
                    except:
                        print('None to return or Error.')
                    print(f"Finished {func.__name__}!")
                    return result
                return wrapper
            except Exception as error_desc: print('Debugger error. ' + str(error_desc))

    @debugger
    def get_file_name(self) -> str:
        try:
            path_parts = self.text_file_path.split(os.path.sep)
            file_name = path_parts[-1]
            self.file_name = os.path.splitext(file_name)[0] 
            return self.file_name
        except Exception as error_desc: print('Error getting filename! ' + str(error_desc))

    @debugger
    def file_open(self) -> list[str]:
        try:
            with open(self.text_file_path, "r", encoding="utf-8") as file:
                self.text = file.readlines()[self.start_line:self.end_line]
                return self.text
        except Exception as error_desc: print('Error opening file! ' + str(error_desc))

    @debugger
    def get_lines_length(self) -> list[tuple[str, int]]:
        try:
            self.lines_length_list = []
            for element in self.text:
                cleaned_line = element.rstrip('\n')
                self.lines_length_list.append((cleaned_line, len(cleaned_line)))
            self.data = self.lines_length_list
            return self.data
        except Exception as error_desc: print('Error getting lines length! ' + str(error_desc))

    @debugger
    def write_db(self) -> str:
        try:
            i = 1 #Id number
            base_query = f'CREATE TABLE IF NOT EXISTS {self.file_name}_database (Id INEGER PRIMARY KEY, Line TEXT NOT NULL, Length TEXT NOT NULL)'
            command = f'INSERT INTO {self.file_name}_database (Id, Line, Length) VALUES (?, ?, ?)'
            with sqlite3.connect(self.db_file_path) as conn:
                conn.execute(base_query)
                for element in self.data:
                    conn.execute(command, (i, element[0], element[1]))
                    i += 1
            return str('Database created.')
        except Exception as error_desc: print('Database error! ' + str(error_desc))

    @debugger
    def read_db(self) -> list[tuple[int, str, int]]:
        try:
            with sqlite3.connect(self.db_file_path) as conn:
                command = f"SELECT * FROM {self.file_name}_database"
                cursor = conn.execute(command)
                self.database_values = cursor.fetchall()
                return self.database_values
        except Exception as error_desc: print('Database read error! ' + str(error_desc))

    #@debugger
    def print_db(self) -> None:
        for element in self.database_values[:self.number_to_print]:
            print(f'Line {element[0]} with lengh of {element[2]}: {element[1]}',end='\n')

    @debugger
    def clear_db(self):
        try:
            i = 1 #Id number
            delete_query = f"DELETE FROM {self.file_name}_database WHERE Id = ? AND Line = ? AND Length = ?"
            with sqlite3.connect(self.db_file_path) as conn:
                for element in self.data:
                    conn.execute(delete_query, (i, element[0], element[1]))
                    i += 1
            return str('Database cleared.')
        except Exception as error_desc: print('Database clear error! ' + str(error_desc))


debugger = False
try:
    if debugger:
        text_file_path = r'C:\Users\Adam\Desktop\Code\Sem 2\shakespeare.txt'
        start_line = 0
        end_line = None
        number_to_print = 55
    else:
        text_file_path = input('Provide a filepath: ')
        text_file_path = os.path.normpath(text_file_path)

        start_line = input('Provide a starting (leave blank for whole file): ')
        start_line = int(start_line) if start_line.strip() else 0

        end_line = input('Provide endline (leave blank for whole file): ')
        end_line = int(end_line) if end_line.strip() else -1

        number_to_print = input('Provide a number of lines to print from the database (leave blank for all): ')
        number_to_print = int(number_to_print) if number_to_print.strip() else -1

except Exception as error_desc: print('Error! ' + str(error_desc))

def get_file_name(path) -> str:
    path_parts = path.split(os.path.sep)
    file_name = path_parts[-1]
    file_name = os.path.splitext(file_name)[0] 
    return file_name

def get_folder_path(path) -> str:
    directory_path = re.match(r'^(.*\\)', path).group(1)
    return directory_path

database_file_name = get_file_name(text_file_path) + str('_database.db')
db_file_path = get_folder_path(text_file_path) + str(database_file_name)


program = LineReader(text_file_path = text_file_path, 
              db_file_path = db_file_path, 
              start_line = start_line,
              end_line = end_line,
              number_to_print = number_to_print
              )

program.get_file_name()
program.file_open()
program.get_lines_length()
program.write_db()
program.read_db()
program.print_db()
program.clear_db()
