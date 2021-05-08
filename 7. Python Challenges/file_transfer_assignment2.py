# Python:   Version 3.9.4
# 
# Author:   Shalondra Rossiter
#
# Purpose:  
#
#
#
 
# File dialogs help you open, save files or directories.
# This is the type of dialog you get when you click file,open.
# This dialog comes out of the module, there’s no need to write
# all the code manually.

import datetime
from datetime import timedelta
import os, shutil

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import *







            
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)
        # From now on we can reference 'Frame' as 'master' and class as 'self'
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(900,400))
        # Making the width and height 'True' allows user to resize the window.
        self.master.title('File Transfer')
        self.master.config(bg='lightpink')

        self.headerlbl = Label(text="Choose a folder to transfer:", font=("Helvetica", 16), fg='white', bg='lightpink')
        self.headerlbl.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.btn_browse1 = Button(text="From", padx=20, command=self.open_window1, font=("Helvetica", 16), fg='white', bg='palevioletred')
        self.btn_browse1.grid(row=2,column=0,padx=(20,10),pady=(20,0))
        self.btn_browse2 = Button(text="To", padx=20, command=self.open_window2, font=("Helvetica", 16), fg='white', bg='palevioletred')
        self.btn_browse2.grid(row=3,column=0,padx=(20,10),pady=(20,0))


        self.btn_transfer = Button(text="Transfer", padx=20,command=self.copy_file, font=("Helvetica", 16), fg='white', bg='palevioletred')
        self.btn_transfer.grid(row=5,column=1,padx=(20,10),pady=(20,0))

        self.msglbl = Label(text="", font=("Helvetica", 16), fg='white', bg='lightpink')
        self.msglbl.grid(row=6,column=1,padx=(30,0),pady=(30,0))

        
        self.dir_src = Entry(width=80)
        self.dir_src.grid(row=2,column=1, padx=10, pady=(30,0))
        self.dir_dst = Entry(width=80)
        self.dir_dst.grid(row=3,column=1, padx=10, pady=(30,0))

        
  
     
        

    ## FUNCTIONS

    def open_window1(self):
        read = fd.askdirectory()
        print(self.dir_src.insert(INSERT, read))


    def open_window2(self):
        read = fd.askdirectory()
        print(self.dir_dst.insert(INSERT, read))


    def copy_file(self):
        source = self.dir_src.get()
        destination = self.dir_dst.get()
        source_files = os.listdir(source)
        for file in source_files:
            abs_path = os.path.join(source,file)
            hours_ago = datetime.datetime.now()-timedelta(hours = 24)
            mod_time = os.path.getmtime(abs_path)
            file_datetime = datetime.datetime.fromtimestamp(mod_time)
            if hours_ago < file_datetime:
                shutil.copy2(source, destination)
                print("The new or modified files have been transfered successfully!")
            else:
                print("There are no new or modified files at this present time.")
       
        
        
        






if __name__  == "__main__":
    win = tk.Tk()
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
