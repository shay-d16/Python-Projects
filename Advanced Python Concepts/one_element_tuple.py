# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Define the difference between a one-element tuple
# and a multi-element tuple and hoow to properly concatenate them.
#


## Don't forget to import sqlite3
import sqlite3


conn = sqlite3.connect('multi_tuple.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_names (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fname TEXT)")
    conn.commit()

    
conn = sqlite3.connect('multi_tuple.db')


## Tuples of names
persons_tuple = ('Kelly','Sally', 'Kevin', 'Adam')

    # To add the names to multi-tuple.db, you have to create a for loop
    # that analyzes the tuple of names and finds only those that end
    # with "y," and then splits the names you want into one-element tuples.


## Loop through each object in the tuple to find the names that end in y.
for x in persons_tuple:
    if x.endswith('y'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therefore (x,)
        # will denote a one-element tuple for each name ending in y.
            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES (?)", (x,))
            print(x)
conn.close()
