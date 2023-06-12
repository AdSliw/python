import sqlite3
# connection = sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\database.db')

# command = "INSERT INTO Student (ID, Name, Surname) VALUES (1, 'Tim', 'Jones')"
# connection.execute(command)
# connection.commit() # all changes are written to the database
# connection.close() # always close the resource

# with sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\database.db') as conn:
#     command = "INSERT INTO Clients (ld, Name, Surname) VALUES (1, Tim' Jones')"


# L1 = [
#     ('Jessica', 'Jones', 'IT', 2020),
#     ('Super', 'Man', 'Heroes', 2018),
#     ( 'Wonder', ' Woman', 'Heroes', 2021),
#     ]


# with sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\Students.db') as conn:
# # are placeholders for the values you are going to supply in the next step
#     command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear) VALUES(?,?,?,?)"
#     for l in L1:
#         conn.execute(command, l)


# ---

# Establish a connection to the SQLite database
# connection = sqlite3.connect('My.db')
# cursor = connection.cursor()

# # Execute the DELETE statement
# delete_query = "DELETE FROM Students WHERE ID IS NULL AND Name = ? AND Surname = ? AND Major = ? AND AdmissionYear = ?"
# L1 = [
#     ('Jessica', 'Jones', 'IT', 2020),
#     ('Super', 'Man', 'Heroes', 2018),
#     ( 'Wonder', ' Woman', 'Heroes', 2021),
#     ]
# for values in L1:
#     cursor.execute(delete_query, values)

# # Commit the changes and close the connection
# connection.commit()

# ---

# with sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\Students.db') as conn:
# # are placeholders for the values you are going to supply in the next step
#     command = "SELECT * FROM Students"
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)

# ---

# with sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\My.db') as conn:
#     conn.execute(
#         "CREATE TABLE IF NOT EXISTS Students ('Id' INTEGER, 'Name' TEXT, 'Surname' TEXT, 'Major' TEXT, 'Admissionyear' INTEGER)")
#     command = 'INSERT INTO STUDENTS (Name, Surname, Major, AdmissionYear) VALUES(?,?,?,?)'
#     delete_query = "DELETE FROM Students WHERE ID IS NULL AND Name = ? AND Surname = ? AND Major = ? AND AdmissionYear = ?"
#     for l in L1:
#         conn.execute(command, l)

# with sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\My.db') as conn:
#     command = "SELECT * FROM Students"
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)

# --- 


# L1 = [
#     ('Jessica', 'Jones', 'IT', 2020),
#     ('Super', 'Man', 'Heroes', 2018),
#     ( 'Wonder', ' Woman', 'Heroes', 2021),
#     ]

# with sqlite3.connect(r'C:\Users\Adam\Desktop\Folders\Studia\Sem 2\Python\UAM\My.db') as conn:
#     conn.execute(
#         '''CREATE TABLE IF NOT EXISTS Students
#         (Id INTEGER PRIMARY KEY,
#         Name TEXT NOT NULL,
#         Surname TEXT NOT NULL,
#         Major TEXT,
#         AdmissionYear INTEGER)'''
#     )
#     delete_query = "DELETE FROM Students WHERE Name = ? AND Surname = ? AND Major = ? AND AdmissionYear = ?"
#     command = 'INSERT INTO Students (Name, Surname, Major, AdmissionYear) VALUES (?, ?, ?, ?)'
#     for data in L1:
#         conn.execute(delete_query, data)