import os, shutil
import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


# File dialogs help you open, save files or directories.
# This is the type of dialog you get when you click file,open.
# This dialog comes out of the module, there’s no need to write
# all the code manually.

import ft2_func


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)
        # From now on we can reference 'Frame' as 'master' and class as 'self'
        self = master
        self.minsize(600,200) #(Height,Width)
        self.maxsize(600,200)
        self.title('File Transfer')
        self.config(bg='lightpink')

    
        self.dir_src = Entry(self,text='',width=60)
        self.dir_src.grid(row=0,column=1,padx=10)
        self.dir_dst = Entry(self,text='',width=60)
        self.dir_dst.grid(row=1,column=1,padx=10)
        self.browse1_btn = Button(self, text="Browse",command= lambda: ft2_func.browse1(self),font=("Helvetica", 12), fg='white', bg='palevioletred')
        self.browse1_btn.grid(row=0,column=0,padx=10,pady=5)
        self.browse2_btn = Button(self, text="Browse",command= lambda: ft2_func.browse2(self),font=("Helvetica", 12), fg='white', bg='palevioletred')
        self.browse2_btn.grid(row=1,column=0,padx=10,pady=5)
        self.check_btn = Button(self,text="Check",command= lambda: ft2_func.check_files(self),font=("Helvetica", 12), fg='white', bg='palevioletred')
        self.check_btn.grid(row=2,column=2,pady=10)  



if __name__  == "__main__":
    win = tk.Tk()
    # call on and pass the class object 'Tk()' to instantiate it as 'win'
    App = ParentWindow(win)
    win.mainloop()
    
