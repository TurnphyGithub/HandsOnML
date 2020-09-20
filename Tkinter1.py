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
        self.create_top_frame()
        self.create_func_frame()

        
    # def create_widgets(self):
    #     self.hi_there = tk.Button(self)
    #     self.hi_there["text"] = "Load the data"
    #     self.hi_there["command"] = load_data_act
    #     self.hi_there.grid(row=self.row_ind, column=0, columnspan=1) 
    #     # self.row_ind +=1
    #     self.quit = tk.Button(self, text="QUIT", fg="red",
    #                           command=self.master.destroy)        
    #     self.quit.grid(row=self.row_ind, column=1, columnspan=1) 
    #     self.row_ind+=1
        
    def create_top_frame(self):
        self.top_frame=tk.Frame(self)
        self.top_frame.grid(row=self.row_ind, column=0)
        self.row_ind+=1
        self.topimg=tk.PhotoImage(file='Images/NR.png')
        tk.Label(self.master, padx=40, pady=10, image=self.topimg).grid(
            row=self.row_ind, column=0, columnspan=1)
    
    def create_func_frame(self):
        self.func_frame=tk.Frame(self)
        self.func_frame.grid(row=self.row_ind, column=0)
        self.row_ind+=1
        LoadDataButton=tk.Button(self.func_frame, text='Load data', command=load_data_act)
        LoadDataButton.grid(row=0, column=0, columnspan=1) 
        QuitButton=tk.Button(self.func_frame, text="QUIT", fg="red",
                             command=self.master.destroy)
        QuitButton.grid(row=0, column=1, columnspan=1)
            

        
        pass
        
        
        

root = tk.Tk()
app = WordRecg(master=root)
app.mainloop()