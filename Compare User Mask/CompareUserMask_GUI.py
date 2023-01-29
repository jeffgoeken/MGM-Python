# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from tkinter import *
from tkinter import ttk
import CompareDataframes as cdf


def callback():
   cdf.main(strUser1.get(),strUser2.get())
    

root = Tk()

strUser1 = StringVar()
strUser2 = StringVar()

ttk.Label(root,text = "User 1 Employee ID").grid(row = 2, column = 2,padx = 10, pady = 5)
ttk.Label(root,text = "User 2 Employee ID").grid(row = 2, column = 6,padx = 10, pady = 5)

etUser1 = ttk.Entry(root,width=16,textvariable=strUser1).grid(row = 2, column = 4,padx = 10, pady = 5)
etUser2 = ttk.Entry(root,width=16,textvariable=strUser2).grid(row = 2, column = 8,padx = 10, pady = 5)

ttk.Button(text = 'Submit',command= callback ).grid(row=4,column = 6,padx = 10, pady = 10)
root.mainloop()

