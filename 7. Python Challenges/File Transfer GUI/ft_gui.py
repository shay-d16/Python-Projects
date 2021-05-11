import tkinter as tk
from tkinter import filedialog 
from tkinter import *
from tkinter import messagebox

import ft_main
import ft_func



def load_gui(self):

        self.browse_btn = Button(self, text="Browse", font=("Helvetica", 12), fg='white', bg='palevioletred' )
        self.browse_btn.grid(row=0,column=0,padx=(10,0),pady=(10,0))
        self.browse_entry = Entry(self,text='',width=45)
        self.browse_entry.grid(row=0,column=1,padx=(10,0),pady=(10,0))

        self.file_lbl = Label(self,text="File name:", font=("Helvetica", 12), fg='palevioletred', bg='lightpink')
        self.file_lbl.grid(row=4,column=0, padx=(10,0), pady=(10,0))
        self.txt_filename = Entry(self,text='',width= 45)
        self.txt_filename.grid(row=4,column=1,padx=(0,0),pady=(10,0))
        
        self.scrollbar1 = Scrollbar(self,orient=VERTICAL)
        self.FolderList = Listbox(self,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.FolderList.yview)
        self.scrollbar1.grid(row=1,column=5,rowspan=3,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.FolderList.grid(row=1,column=0,rowspan=3,columnspan=5,padx=(10,10),pady=(10,0),sticky=N+E+S+W)



        
        ## OPEN BUTTON
        self.btn_open = Button(self,width=12,height=2,text="Open",fg='white', bg='palevioletred')
        self.btn_open.grid(row=0,column=7,padx=(20,10),pady=(10,10),sticky=W)

        ## EDIT BUTTON
        self.btn_edit = Button(self,width=12,height=2,text="Edit",fg='white', bg='palevioletred')
        self.btn_edit.grid(row=1,column=7,padx=(20,10),pady=(10,10),sticky=W)

        ## CANCEL BUTTON
        self.btn_cancel = Button(self,width=12,height=2,text="Cancel",fg='white', bg='palevioletred')
        self.btn_cancel.grid(row=2,column=7,columnspan=1,padx=(20,10),pady=(10,10),sticky=W)

        ## CHECK BUTTON
        self.btn_check = Button(self,width=12,height=2,text="Check",fg='white', bg='palevioletred')
        self.btn_check.grid(row=3,column=7,padx=(20,0),pady=(10,10),sticky=W)

        ## CLOSE BUTTON
        self.btn_close = Button(self,width=12,height=2,text="Close",fg='white', bg='palevioletred')
        self.btn_close.grid(row=4,column=7,columnspan=1,padx=(20,0),pady=(10,10),sticky=W)
        






if __name__ == "__main__":
    pass

