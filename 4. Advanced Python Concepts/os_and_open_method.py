# Make sure to import os so that Python will have the ability to use
# and access whatever method we're using 
import os


# Make sure that when you call on a class and you want to access
# it's methods within the class, you have mention the class first,
# then put a period, then the method. EX: print(os.getcwd())

def writeData(): # similar to the open() process
    data = '\nHello World!'
    # we're going to 'write', but unfortunately that would overwrite on top of it
    # so we have to use 'append'
    # open for writing, appending to the end of the file if it exists
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    # While this test.txt file is open we call it 'f' for file
    with open('test.txt', 'r') as f:
        data = f.read() # While file is open, read it and store it in data variable
        print(data)
        # To make sure you aren't creating any memory leaks with you software
        # you need to make sure you close that file when you're done
        f.close()


if __name__ == "__main__":
    writeData()
    openFile()
