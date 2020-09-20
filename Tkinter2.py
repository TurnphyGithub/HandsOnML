# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:41:41 2018
ML with interface
@author: Turnphy
"""

import tkinter as tk
from WordRecognizer import *
class WordRecg(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.grid(row=0, column=0, columnspan=2) 
        self.row_ind=1  
        self.create00_top_frame()
        
        self.create01_func_frame()

        
    def create00_top_frame(self):
        self.top_frame=tk.Frame(self.master)
        self.top_frame.grid(row=self.row_ind, column=0)
        self.row_ind+=1
        self.topimg=tk.PhotoImage(file='Images/NR.png')
        tk.Label(self.master, padx=40, pady=10, image=self.topimg).grid(
            row=0, column=0, columnspan=1)
    
    def create01_func_frame(self):
        self.func_frame=tk.Frame(self.master)
        self.func_frame.grid(row=self.row_ind, column=0)
        self.row_ind+=1
        LoadDataButton=tk.Button(self.func_frame,\
                                 text='Load data', command=load_data_act)
        LoadDataButton.grid(row=0, column=0, padx=5, pady=5, columnspan=1) 
        QuitButton=tk.Button(self.func_frame, text="QUIT", fg="red",
                             command=self.master.destroy)
        QuitButton.grid(row=0, column=1, padx=5, pady=5, columnspan=1) 
        
        tk.Label(self.func_frame, text='Show an example:',  padx=5, \
                 pady=5).grid(row=1, column=0, columnspan=2)
        num_input=tk.Entry(self.func_frame,  width=10)
        num_input.grid(row=2, column=0, padx=5, pady=5,columnspan=1)
        GenButton=tk.Button(self.func_frame,\
                                 text='Generate', command=load_data_act)
        GenButton.grid(row=2, column=1, padx=5, pady=5, columnspan=1) 

        

root = tk.Tk()
app = WordRecg(master=root)
app.mainloop()