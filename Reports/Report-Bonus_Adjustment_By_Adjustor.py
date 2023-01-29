import pyodbc
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
import logging
timestamp = (datetime.now()).strftime("%Y-%m-%d %H%M")
logfilepath = (rf"./logs/SQLErr{timestamp}.log")
filepath = (rf"C:\Users\jgoeken\OneDrive - MGM Resorts International\Uploads\Bonus Adjustment by Adjustor {timestamp}.xlsx")

#create and configure the logger

logging.basicConfig(filename = logfilepath,format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)



def AssignVariable():
    root.quit()
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=s1playrpt03p;'
                      'Database=playermanagement;'
                      'Trusted_Connection=yes;')
        logger.info("Connection Successful")
    except pyodbc.Error as err:
        logger.exception("Connection Failed")
        messagebox.showerror("Connection Failed", err)

    query = (f"exec Report_RS_BonusAdjustmentByAdjuster '{strStartDate.get()}','{strEndDate.get()}' ,null,null,{strSiteID.get()}")


    df = pd.read_sql_query(query, conn)
    logger.info("SQL Query Successful")


    print(df)
    
    df1= df.loc[:1048573]
    df2 = df.loc[1048574:2097146]
    #df3 = df.loc[2097147:3145720]
    #df4 = df.loc[3145721:4194294]
    #df5 = df.loc[4194295:5242868]





    with pd.ExcelWriter(filepath) as writer:
        df1.to_excel(writer, sheet_name='Sheet 1')
        df2.to_excel(writer, sheet_name='Sheet 2')
        #df3.to_excel(writer, sheet_name= 'Sheet 3')
        #df4.to_excel(writer, sheet_name= 'Sheet 4')
        #df5.to_excel(writer, sheet_name= 'Sheet 5')
                     
    root.destroy()
    
    
    
#**********GUI**************
root = Tk()
strStartDate = StringVar()
strEndDate = StringVar()
strSiteID = StringVar()
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
