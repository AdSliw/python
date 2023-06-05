import sqlite3
connection = sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\database.db')

command = "INSERT INTO Student (Id, Name, Surname) VALUES (1, 'Tim', 'Jones')"
connection.execute(command)
connection.commit() # all changes are written to the database
connection.close() # always close the resource