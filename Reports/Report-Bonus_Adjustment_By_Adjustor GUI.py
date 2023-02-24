import pyodbc
import pandas as pd
import openpyxl
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=playdb01r;'
                      'Database=PlayerManagement;'
                      'Trusted_Connection=yes;')
SiteQuery = 'SELECT Description,SiteID from Site (Nolock)'
ReportQuery ="select name from sys.procedures where name like 'REPORT_%' order by name"
Sites = pd.read_sql_query(SiteQuery, conn).reset_index(drop=True)
Reports = pd.read_sql_query(ReportQuery, conn)
print(Reports)

dataTable = ({
    'StartDate':[],
    'EndDate':[],
    'siteID':[],
    'Property':[]
     })
df = pd.DataFrame(dataTable)

def buildStartDateText(lblStartDatetxt,strStartDate):
    lblStartDatetxt += strStartDate
    return lblStartDatetxt

def AssignVariable():
    print(strStartDate.get())
    print(strEndDate.get())
    print(strSiteID.get())
    print(strReportName.get())
    lblStartDatetxt = strStartDate.get()
    
    lblStartDate.set(lblStartDatetxt)

   

root = Tk()

lblEndDatetxt = ''
lblSitetxt = ''
lblReporttxt = ''
strStartDate = StringVar(root)
strEndDate = StringVar(root)
strSiteID = StringVar(root)
strReportName = StringVar(root)
root.config(bg='lightblue')

lblStartDatetxt = ''


ttk.Label(root,text = 'Start Date',background='lightblue').grid(row=0,column=0,sticky='ew',padx=10,pady=5)
ttk.Label(root,text = 'End Date Date',background='lightblue').grid(row=0,column=2,sticky='ew',padx=10,pady=5)
ttk.Label(root,text = 'Site',background='lightblue').grid(row=0,column=4,sticky='ew',padx=10,pady=5)
ttk.Label(root,text = 'Report',background='lightblue').grid(row=0,column=6,sticky='ew',padx=10,pady=5)
dpStartDate = DateEntry(root,textvariable=strStartDate).grid(row=0,column = 1,padx=10,pady=5)
dpEndDate = DateEntry(root,textvariable=strEndDate).grid(row=0,column = 3,padx=10,pady=5)
ttk.Combobox(root,width=20,textvariable=strSiteID,values=Sites.loc[:,'Description'].to_list()).grid(row=0,column = 5,padx=10,pady=5,sticky='w')
ttk.Combobox(root,width=40,height=20,textvariable=strReportName,values=Reports.loc[:,'name'].to_list()).grid(row=0,column = 7,padx=10,pady=5,sticky='w')
btnGO = ttk.Button(root,text = "Request",command = AssignVariable).grid(row=0,column=9,padx=10,pady=10)

lblStartDate = ttk.Label(root,text = lblStartDatetxt,background='lightblue').grid(row=1,column=1,sticky='w',padx=10,pady=5,columnspan=9)


root.mainloop()
