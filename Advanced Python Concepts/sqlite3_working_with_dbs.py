
import sqlite3

    # Remember that whenever you're using a class, you call the class first,
    # then a period, and then the method inside the class

    # We'll use the connect() method to connect to the database file
conn = sqlite3.connect('test.db')

    # With loop saying 'while we have this connection open,
    # do the following lines of code until we close the session
with conn:
    # The cursor is what's going to be operating on the actual
    # database when we want to give commands to execute on the DB
    cur = conn.cursor() # We're accessing the cursor object as variable 'cur'
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()



conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Bob', 'Smith', 'bsmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sally', 'May', 'sallymay@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Kevin', 'Bacon', 'kbacon@rocketmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson: # Use for loop to unpack the data and store it in 'msg' string
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
    

