import pandas as pd
import pyodbc
from tkinter import filedialog
import openpyxl

def main(User1,User2):
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=playdb01p;'
                        'Database=PlayerManagement;'
                        'Trusted_Connection=yes;')


    #User1 = input('Please enter User 1s EmployeeID: ')
    #User2 = input('Please enter User 2s EmployeeID: ')


    query1 = (f"""
    SELECT  ABU.LoginName, AUM.*,mask.Mask 
    from ABSUSER as ABU (nolock)
    join ABSUSERMASK (nolock) as AUM on ABU.UserID = AUM.UserID
    join mask (nolock) on mask.MaskNum = AUM.MaskNum
    where ABU.LoginName = '{User1}'""")

    user1Data = pd.read_sql_query(query1, conn)
    #print(user1Data)

    query2 = (f""" 
    SELECT  ABU.LoginName, AUM.*,mask.Mask 
    from ABSUSER as ABU (nolock)
    join ABSUSERMASK (nolock) as AUM on ABU.UserID = AUM.UserID
    join mask (nolock) on mask.MaskNum = AUM.MaskNum
    where ABU.LoginName = '{User2}'""")
    user2Data = pd.read_sql_query(query2,conn)
    #print(user2Data)

    # Compare the two dataframes

    # Compare the two dataframes
    # If the two dataframes are not the same, print the differences
    # If the two dataframes are the same, print "The two dataframes are the same"
    CombinePermissions = user2Data.merge(user1Data, on = ['SiteID','MaskNum'], how = 'outer', indicator = True)
    DifferentPermissions = CombinePermissions[CombinePermissions['_merge'] != 'both']
    #print(CombinePermissions)
    print(DifferentPermissions)

    FilePath = (filedialog.asksaveasfilename(defaultextension= '.xlsx' ,initialdir = "/Documents",title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*"))))
    print(FilePath)
    with pd.ExcelWriter(FilePath,mode='w') as writer:
            DifferentPermissions.to_excel(writer, sheet_name= 'DifferentPermissions')
            CombinePermissions.to_excel(writer, sheet_name= 'CombinePermissions')



