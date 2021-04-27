# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Database Submission Assignment. Meet the following requirements
# given to me by the Tech Academy.
#


## 1. Your script will need to use Python 3 and the sqlite3 module.
import sqlite3


    # Remember that whenever you're using a class, you call the class first,
    # then a period, and then the method inside the class

    # Use the connect() method to connect to the database file
conn = sqlite3.connect('Assignment.db')
    

## 2. Your database will require 2 fields: an auto-increment primary integer
## field and a field with the data type “string.”
cur = conn.cursor() # The cursor is what's going to be operating on the actual
                    # database when you want to give commands to execute on the DB
cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    file_name TEXT)")
conn.commit()


conn = sqlite3.connect('Assignment.db')


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

## 3. Your script will need to read from the supplied list of file names at 
## the bottom of this page and determine only the files from the list which
## end with a “.txt” file extension
## 4. Next, your script should add those file names from the list ending with
## “.txt” file extension within your database.
## 5. Finally, your script should legibly print the qualifying text files to the console.

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (x,))
            print(x)
    
conn.close()

