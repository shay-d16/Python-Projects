import sys, os, shutil
import glob
import os.path, time
import tkinter as tk
from tkinter import filedialog as fd

class ParentWindow(Frame):
    def __init__ (self, master):
        # From now on we can reference 'Frame' as 'master' and class as 'self'
        Frame.__init__ (self)
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(900,400))
        # Making the width and height 'True' allows user to resize the window.
        self.master.title('File Explorer')
        self.master.config(bg='lightpink')

    ## BUTTONS
        self.btnBrowse = Button(self.master, text="Browse...",width=8,height=1,command=self.browse, font=("Helvetica", 16), fg='white', bg='palevioletred')
        self.btnBrowse.grid(row=4,column=0,padx(0,0),pady=(0,0))
        
    
        

    ## ENTRY
        self.entry= Entry(win, text="", width=70)
        self.entry.grid(row=4,column=1, padx=(30,0), pady=(0,0), sticky=N+W)

        self.entry= Entry(win, text="", width=70)
        self.entry.grid(row=5,column=1, padx=(30,0), pady=(0,0), sticky=N+W)
    


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

