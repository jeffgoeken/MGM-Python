# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:15:18 2022

@author: jgoeken
"""

from tkinter import *
import os
# Create Root Window
root = Tk()

os.system("TASKKILL /f /im patron.exe")

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

#geometry Method
pane.pack(fill = BOTH, expand = True)

# Tkinter string variable
# able to store any string value
v = StringVar(pane, "1")

# Dictionary to create multiple buttons
values = {"Aria" : "V00WAARACE11P",
        "Beau Rivage" : "V21WABRACE11P",
        "Bellagio" : "V00WABGACE11P",
        "Borgata" : "V41WABGTAACE11P",
        "Cosmopolitan":"TBD",
        "Detroit" : "V31WADTACE11P",
        "Empire" : "V43WAACE11P",
        "Excalibur":"V00WAEXACE11P",
        "Gold Strike" : "V38WAGTACE11P",
        "Luxor" : "V00WALXACE11P",
        "Mandalay Bay":"V00WAMBACE11P",        
        "MGM Las Vegas" : "V00WAMMACE11P",
        "Mirage" : "V00WAMRACE11P",
        "National Harbor" : "V34WAACE11P",
        "New York, New York" : "V00WANYACE11P",
        "Northfield Park" : "V44WAACE11P",
        "Park MGM" : "V00WAMCACE11P",
        "Springfield" : "V33WAACE11P",
        "V'Dara" : "V00WAVDACE11P",
        }

# Loop is used to create multiple Radiobuttons
for (text, value) in values.items():
    Radiobutton(pane, text = text, variable = v,
        value = value, indicatoron= 0, 
        background= "light blue", command=GetDataSource).pack(fill = BOTH, expand = True, padx=10,pady=2)

# Close event loop
root.mainloop()

print(values.items())
