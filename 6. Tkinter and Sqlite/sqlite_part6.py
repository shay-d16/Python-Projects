import sqlite3

# get personal data from user and insert into a tuple
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

# execute insert statements for supplied person data
with sqlite3.connect('sqlite_assignment.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?,?,?)", personData)
