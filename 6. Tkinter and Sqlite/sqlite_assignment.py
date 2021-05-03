# Python:       Version 3.9.4
#
# Author:       Shalondra Rossiter
#
# Purpose:
#
#
#


# There are many different variations of SQL.
# Some are suited to certain purposes better than others.
# A simple, lightweight version of SQL is SQLite, which
# runs directly on your machine and comes bundled with
# Python automatically.


# SQLite is usually used within applications for small internal
# storage tasks but can also be useful for testing SQL code before
# setting up an application to use a larger database.


# In order to communicate with SQLite, we need to import the SQLite
# module and connect to a database.


import sqlite3

connection = sqlite3.connect("sqlite_assignment.db")

c = connection.cursor()
# This line instantiates a Cursor object. A cursor is a control structure
# that enables operations on a database. Our Cursor object 'c' will let us
# execute commands on our SQL database 'test_database' and return the results.

# Now we can easily execute regular SQL statements on the database through the cursor
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
# This line creates a new table named People and inserts three new columns into the table:
# text for storing each person’s FirstName, another text field to store the LastName,
# and an integer to store Age.


