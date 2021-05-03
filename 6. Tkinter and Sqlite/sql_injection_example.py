import sqlite3

# get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))


# execute insert statements for supplied person data
with sqlite3.connect('sqlite_assignment.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
    # Notice how we had to change age into an integer to
    # make sure that it was a valid age, but then we had
    # to change it back into a string in order to concatenate
    # it with the rest of the line; this is because we created
    # the line by adding a bunch of strings together, including
    # using single quotation marks to denote strings within our string.



# If you’re still not clear how this works, try inserting a person into
# the table, then print (line) to see how the full line of SQL code looks.
