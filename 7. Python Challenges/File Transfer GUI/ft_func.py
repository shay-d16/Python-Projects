#
#
#
#
#
#
#

import os, shutil
import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


import ft_main
import ft_gui


def browse(self):
        bf = tk.filedialog.askdirectory()
        return bf


        
        
        


def edit_file(self):
        read = tk.filedialog.askopenfile(mode="a")
        return read


def callback(self):
        name = tk.filedialog.askopenfilename()
        print(self.filename.insert(INSERT, name))


def check_files(self):
    for file in source_files:
        abs_path = os.path.join(source,file)
        hours_ago = datetime.datetime.now()-timedelta(hours = 24)
        mod_time = os.path.getmtime(abs_path)
        file_datetime = datetime.datetime.fromtimestamp(mod_time)
        if hours_ago < file_datetime:
            shutil.copy(source, destination)
            messagebox.showinfo("The new or modified files have been transfered successfully!")
        else:
            messagebox.showinfo("There are no new or modified files at this present time.")
       
        
def center_window(self, w, h):
    # pass in the tkinter frame (master) reference and the w and h
    
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    # get user's screen width and height
    
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    # calculate x and y coordinates to paint the app centered on the user's screen
    centerGeo = self.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    # This will catch if the user's clicks on the window upper-right 'X' to ensure
    # they want to close.
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.destroy()
        os._exit(0)
        # This closes the app


 



if __name__ == "__main__":
    pass
