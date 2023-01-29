# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:15:18 2022

@author: jgoeken
"""

#mport Modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os

# Create Root Window
root = Tk()
root.title ('PySwitcher')
root.configure(bg ='white')

photo = tk.PhotoImage(master=root,file=r'C:\Users\jgoeken\OneDrive - MGM Resorts International\Pictures\MGMLogo.png')

image_label = ttk.Label(
    root,
    image=photo,
    background= 'white'
    
)
image_label.pack(side = 'top', fill = X)

#Check for open Patron applications
Patrontest = bool(os.popen('TASKLIST |find  "Patron.exe"').read())
print(Patrontest)
if Patrontest == True:
    message = """
    Another instance of Patron detected!
    Please close all open Patron Management
    applications before selecting a 
    property.
    """
    messagebox.showwarning(title="Patron Instance Detected",message=message)



def GetDataSource():

    DataSource = v.get()
    DBConnectInfo = """
     <?xml version="1.0" encoding="utf-8"?>
        <configuration>
          <system.runtime.remoting>
             <application>
                <client>
                   <wellknown type="Igt.Egs.Data.EGSConnInfoStore, DBConnInfoStore" url="http://{}:8989/EGSConnInfoStore.rem"></wellknown>
                </client>
             </application>
          </system.runtime.remoting>
          <startup>
             <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.8"></supportedRuntime>
          </startup>
       </configuration>
    """
    print(DBConnectInfo.format(DataSource))

    DBConnectFile = open ("C:\Program Files (x86)\Common Files\IGT Systems\DbConnInfoManager.dll.config","w")
    DBConnectFile.write(DBConnectInfo.format(DataSource))
    DBConnectFile.close()
    os.startfile('C:\\Program Files (x86)\\IGT Systems\\Patron Management\\Patron.exe')   
    root.destroy()
        

# Create Frame inside Root Window
pane = Frame(root)
pane.title = 'PySwitcher'
#geometry Method
pane.pack(fill = BOTH, expand = True,padx=10,pady=5)

# Tkinter string variable
# able to store any string value
v = StringVar(pane, "1")

# Dictionary to create multiple buttons
values = {"Aria" : "V00WAARACE11P",
        "Beau Rivage" : "V21WABRACE11P",
        "Bellagio" : "V00WABGACE11P",
        "Borgata" : "V41WABGTAACE11P",
        #"Cosmopolitan":"TBD",
        "Detroit" : "V31WADTACE11P",
        "Empire" : "V43WAACE11P",
        "Excalibur":"V00WAEXACE11P",
        "Gold Strike" : "V38WAGTACE11P",
        "Luxor" : "V00WALXACE11P",
        "Mandalay Bay":"V00WAMBACE11P",        
        "MGM Las Vegas" : "V00WAMMACE11P",
        "Mirage" : "V00WAMRACE11P",
        "National Harbor" : "V33WAACE11P",
        "New York, NY" : "V00WANYACE11P",
        "Northfield Park" : "V44WAACE11P",
        "Park MGM" : "V00WAMCACE11P",
        "Springfield" : "V34WAACE11P",
        "V'Dara" : "V00WAVDACE11P",
        "Pre-Prod" : "VMBGACE01R",
        "S7 Pre-Prod" : "V36WAMRACE11R"
        }

#Build Form

#Label(pane,text = "PySwitcher",
      #background = "cyan",
      #font="Arial,20").grid(row=1,columnspan=3,sticky = 'ew')

# Loop is used to create multiple Radiobuttons
r=1
c=0
for (text, value) in values.items():
    Radiobutton(pane, text = text, variable = v,
        value = value, indicatoron= 0, 
        background= "light blue",
        font="Arial,14",
        command=GetDataSource).grid(row = r, column=c,sticky='ew', padx=2,pady=2)
    if c ==2:
        c=0
        r +=1
    else:
        c += 1
# Close event loop

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
   
#root.mainloop()

print(values.items())
