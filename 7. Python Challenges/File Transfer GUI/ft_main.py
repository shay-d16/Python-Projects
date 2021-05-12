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
from tkinter.filedialog import askdirectory
from tkinter import messagebox as mb
from tkinter import *

import ft_gui
import ft_func





            
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)
        # From now on we can reference 'Frame' as 'master' and class as 'self'
        self = master
        self.minsize(550,350) #(Height,Width)
        self.maxsize(550,350)
        ft_func.center_window(self,500,350)
        self.title('File Transfer')
        self.config(bg='lightpink')

        self.protocol("WM_DELETE_WINDOW", lambda: ft_func.ask_quit(self))

        ft_gui.load_gui(self) 



if __name__  == "__main__":
    win = tk.Tk()
    # call on and pass the class object 'Tk()' to instantiate it as 'win'
    App = ParentWindow(win)
    win.mainloop()
    
    v = StringVar()
    
