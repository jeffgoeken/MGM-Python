import pyodbc
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry



def AssignVariable():
    root.quit()

    print(strStartDate.get())
    print(strEndDate.get())
    print(strSiteID.get())

root = Tk()

strStartDate = StringVar()
strEndDate = StringVar()
strSitID = StringVar()
root.config(bg='lightblue')

ttk.Label(root,text = 'Start Date',background='lightblue').grid(row=2,column=1,sticky='ew',padx=10,pady=5)
ttk.Label(root,text = 'End Date Date',background='lightblue').grid(row=2,column=4,sticky='ew',padx=10,pady=5)
ttk.Label(root,text = 'SiteID',background='lightblue').grid(row=4,column=1,sticky='ew',padx=10,pady=5)
dpStartDate = DateEntry(root,textvariable=strStartDate).grid(row=2,column = 2,padx=10,pady=5)
dpEndDate = DateEntry(root,textvariable=strEndDate).grid(row=2,column = 5,padx=10,pady=5)
#ttk.Entry(root,width=15,textvariable=strStartDate).grid(row=2,column = 2,padx=10,pady=5)
#ttk.Entry(root,width=15,textvariable=strEndDate).grid(row=3,column = 2,padx=10,pady=5)
ttk.Entry(root,width=5,textvariable=strSiteID).grid(row=4,column = 2,padx=10,pady=5,sticky='w')
btnGO = ttk.Button(root,text = "Submit",command = AssignVariable).grid(row=6,column=1,padx=10,pady=10,columnspan=5)
root.mainloop()