import shutil, os
import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox


import ft2_main


def browse1(self):
    bf = tk.filedialog.askdirectory()
    self.dir_src.delete(0, END)
    self.dir_src.insert(0, bf)

def browse2(self):
    bf = tk.filedialog.askdirectory()
    self.dir_dst.delete(0, END)
    self.dir_dst.insert(0, bf)

def check_files(self):
        source = self.dir_src
        destination = self.dir_dst
        source_files = os.listdir(source)
        dest_files = os.listdir(destination)    
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
           
if __name__ == "__main__":
    pass
