# Python 3.9.4
#
# Author: Shalondra Rossiter
#
# Purpose: Using the Tkinter model to create Graphical User Interfaces (GUIs).
#

# For Python itself we have to import the Tkinter module
import tkinter
from tkinter import *
# This imports Tkinter and all (*) of its widgets. 



## CLASS OBJECT

# The 'Frame' happens to be the parent class within Tkinter, so we'll be
# inheriting what Tkinter has within this class.
class ParentWindow(Frame):
    def __init__ (self, master):
        # From now on we can reference 'Frame' as 'master' and class as 'self'
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        # Making the width and height 'True' allows user to resize the window.
        self.master.geometry('{}x{}'.format(700,400))
        # This set the size of the window when it's open.
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightpink')
        # This makes the background of the window dark gray.

    ## STRING VARIABLES
        # We are going to create text boxes, and this is how we can affect
        # what's in those text boxes, by storing info into a string, and
        #putting it into that text box. 
        self.varFName = StringVar()
        # 'StringVar' = "String Variable"
        self.varLName = StringVar()
        

        ### DELETED CODE, HERE FOR REFERENCE            
            # self.varFName.set('Shay')
                # set() means we are going to assign a value
            # self.varLName.set('Davis')
                # Remember to stay consitent with our code; In the lines above
                # we added 'self'

            # print(self.varFName.get())
                # To set the value we used 'set()' and to get the value,
                # we use 'get()'. We don't need to put anything inside the
                # parenthesis because we're getting whatever is in it already.
            # print(self.varLName.get())
                # If you forget to add the 'self' part to the variable,
                # you would recieve and error message in the console, because
                # without 'self' the console doesn't know how to access that object.
        ### END DELETED CODE


    ## LABELS
        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightpink')
        # Label() invokes the label widget.
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))
        # 'padx' and 'pady' are for Tkinter padding, with 10 and 0 being "10 and 0 pixels".
        # The 'x' and 'y' part of the syntax refers to horizontal and
        # verticle, respectively.
        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightpink')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightpink')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

    ## TEXT BOXES
        # The open-close parenthesis is calling that particular class,
        # but that class has several different things that we can use
        # to configure it. 
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        # So to configure the text box, the first thing you
        # need to do is tell it where it needs to go. So we attatch it to
        # self.master ("place this entry on master")

        # NOTE: In above line of code, we aren't going to give 'text' one value.
        # We want it to be able to change, so we create a variable object for it.
        # So now 'text' will equal whatever is stored in the 'self.varFName' value.
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))  

        ### DELETED CODE:
            # self.txtFName.pack()
                # There are different types of geometry managers, which is what you would
                # use to paint something on a form or a window. In this case we're using 
                # 'pack()' to paint the window with the above styling parameters.
        ### END DELETED CODE
            
         
        self.txtLName = Entry(self.master,text=self.varLName,font=("Helvetica", 16),fg='black',bg='lightblue')

        ### DELETED CODE:
            # self.txtLName.pack()
        ### END DELETED CODE
        
        self.txtLName.grid(row=1,column=1,padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit",width=10,height=2,command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0), pady=(30,0),sticky=NE)
        # Sticky tells the console where we want this to "stick" in the window.
        # If you want it to stick "up and over" you'd type NE as in North-East
        # (North being up, East being to the right).

## SUBMIT AND CANCEL BUTTONS AND FUNCTIONS
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2,command=self.cancel)
        self.btnCancel.grid(row=2,column=1,padx=(0,90), pady=(30,0),sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        # Remember, we are going to be getting the values from the text boxes,
        # so to get the values from said text boxes, we're going to get the values
        # and store them in a temporary variable. It's not the text boxes you're getting
        # the values from. It's the values from the variable that was assigned to it,
        # which in this case is 'self.varFName'. And the get() method gets whatever
        # value is being held by this variable. Whatever the value is at the time
        # the user presses the submit button will get stored into 'fn'.
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello, {} {}!'.format(fn,ln))
        # To get something to change dynamically in the middle of your program, while
        # it's running, you use its configuration.
    def cancel(self):
        self.master.destroy()
        # This closes the self.master window.

        
## INSTANTIATION
 
# Always make sure to use this line of code to control program flow.
# Python will ignore any other code written above and skip strain down
# to this line of code, and call the next function after this line.

if __name__  == "__main__":
    # call on and pass the class object 'Tk()' to instantiate it as 'root'
    root = Tk()
    # the next syntax when you're dealing with Tkinter will attatch
    # ParentWindow to 'root', so now this ParentWindow Frame is coming
    # from Tkinter because 'Frame' is Tkinter's main class. We named
    # it 'root', we attatched it to our 'ParentWindow'. Once our class is
    # instantiated with the Tkinter class instantiated, we pass it to 'App'
    App = ParentWindow(root)
    # Wihtout this next line of code it will launch and then immediately close,
    # because the syntax that keeps it "alive" is 'mainloop()'. If we dont do
    # this 'mainloop()' function, it won't coninuously run, meaning the window
    # will simply pop up and disappear.
    root.mainloop()

    
    
