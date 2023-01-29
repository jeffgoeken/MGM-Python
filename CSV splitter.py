# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from tkinter import *
from tkinter import ttk


root = Tk()
progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200,mode = 'indeterminate')
progressbar.pack()
progressbar.start()

report = pd.read_csv(r"C:\Users\jgoeken\Downloads\Bonus Adjustment by Adjustor.csv", skiprows = 2
                     )
print(report)
reportend = (len(report.index)-1048575)

df1= report.head(1048576)
df2 = report.tail(reportend)

print(len(df1.index))
print(len(df2.index))




with pd.ExcelWriter(r'C:/Users/jgoeken/Downloads/October.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Hi')
    df2.to_excel(writer, sheet_name='KP')
progressbar.stop()   
    
#report.head(1048576).to_excel(r"C:/Users/jgoeken/Downloads/report.xlsx")
