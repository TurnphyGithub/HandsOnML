# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:12:28 2020

@author: Turnphy
"""
from sklearn.datasets import fetch_openml # for func 
import matplotlib as mpl
import matplotlib.pyplot as plt
import tkinter as tk

def load_data():  
    global mnist
    mnist = fetch_openml('mnist_784', version=1)
    print('Data load successfuly ...')
    print(mnist.keys())
    return 
# mnist=load_data()
    
def show_data_info(mnist):
    # X, y = mnist["data"], mnist["target"]
    # X.shape
    # y.shape
    str1='There are '+str(123)+' training examples.'
    messages=tk.Toplevel()
    messages.minsize(width=100, height=100)
    messages.title('Data information:')
    tk.Label(messages, text=str1).grid(row=0, column=0)
    canvas = tk.Canvas(messages, width=400, height=400)
    
    canvas.grid(row=1, column=0)
    img=tk.PhotoImage(file='WR.png')
    width, height=380,391
    canvas.create_image(width/2, height/2,image=img, anchor='center')
    canvas.image = img
    return

def load_data_act():
    global mnist
    mnist=[1,2]
    # load_data()
    show_data_info(mnist)


