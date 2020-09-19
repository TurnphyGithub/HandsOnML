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
        self.grid(row=0, column=0) #, columnspan=2) 
        self.top_img()
        self.create_widgets()
        

    def top_img(self):
        self.topimg=tk.PhotoImage(file='NR.png')
        tk.Label(self, padx=40, pady=10, image=self.topimg).grid(row=1, column=0)
        
        
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Load the data"
        self.hi_there["command"] = load_data_act
        self.hi_there.grid(row=2, column=0)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        
        self.quit.grid(row=3, column=0) #, columnspan=2) 
    
    def load_data(self):
        return

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = WordRecg(master=root)
app.mainloop()