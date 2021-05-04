# Python:   Version 3.9.4
#
# Author:   Shalondra Rossiter
#
# Purpose:  1. Create a Tkinter GUI that allows the user to input
#           text and initiate the web page generation process.
#           2. Generate a web page that sets the user's input as the
#           body text for the web page.
#           3. Opens the generated web page in the browser.


# Remember to import both the Tkinter and Webbrower modules.
import tkinter as tk
from tkinter import *
import webbrowser as wb

# The 'Frame' happens to be the parent class within Tkinter, so we'll be
# inheriting what Tkinter has within this class.
class ParentWindow(Frame):
    def __init__ (self, master):
        # From now on we can reference 'Frame' as 'master' and class as 'self'
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        # Making the width and height 'True' allows user to resize the window.
        self.master.geometry('{}x{}'.format(900,400))
        # This set the size of the window when it's open.
        self.master.title('Web Page Generator')
        self.master.config(bg='lightpink')
        # This makes the background of the window light pink.

     

        
    ## STRING VARIABLE
        self.varBody = StringVar()


    ## LABEL

        self.entrylbl = Label(self.master,text="Set the text of the web page yourself! Type whatever you want below!", font=("Helvetica", 16), fg='white', bg='lightpink')
        self.entrylbl.grid(row=0, column=1, padx=(30,0), pady=(30,0))

    ## ENTRY
        self.entry= Entry(win, text="", width=70)
        self.entry.grid(row=4,column=1, padx=(30,0), pady=(0,0))


    ## ENTER BUTTON
        self.btnEnter = Button(self.master, text="Enter",width=10,height=1,command=self.enter, font=("Helvetica", 16), fg='white', bg='palevioletred')
        self.btnEnter.grid(row=4,column=2,padx=(0,0), pady=(0,0))




    def enter(self):
        # To create a new file in Python, use the open() method
        wp = open("wp_generator.html", "a")
        # "a" is for Append, and it will create a file if the specified file does not exist.
        url = 'wp_generator.html'
        w = open(url, "w")
        # "w" is for Write, and it will overwrite any existing content.
        bt = self.entry.get()
        # This will retrieve whatever text is in the entry box at the time Enter is pressed.
        w.write("""
                <html style="text-align: center; color: palevioletred;">
                    <body>
                        <h1 style="margin-top:50px;">{}</h1>
                    </body>
                </html>
                """.format(bt))
        
        # Open URL in a new tab, if a browser window is already open.
        wb.open_new_tab(url)
        








if __name__  == "__main__":
    win = Tk()
        # call on and pass the class object 'Tk()' to instantiate it as 'win'
    App = ParentWindow(win)
        # When you're dealing with Tkinter, this syntax will attatch
        # ParentWindow to 'win', so now this ParentWindow Frame is coming
        # from Tkinter because 'Frame' is Tkinter's main class. We named
        # it 'win', we attatched it to our 'ParentWindow'. Once our class is
        # instantiated with the Tkinter class instantiated, we pass it to 'App'
    win.mainloop()
        # Wihtout this line of code it will launch and then immediately close,
        # because the syntax that keeps it "alive" is 'mainloop()'. If we dont do
        # this 'mainloop()' function, it won't coninuously run, meaning the window
        # will simply pop up and disappear.

    
