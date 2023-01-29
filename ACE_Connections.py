# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyodbc 
import pandas as pd
import datetime as dt
x = dt.datetime.now()
filedate = x.strftime("%m/%d/%y %I:%M:%S %p")
print(x)
print(filedate)
path = "C:\\Users\\jgoeken\\Documents\\Self-Limit report{}.csv"

print(path.format(filedate))
htmlout = """
<style>
body {font-family:Arial;}
td, th, table { border: 1px solid lightgrey;border-collapse: collapse;}
h2 {color:blue;font-family:Arial;}	
th {color : white; 
background-color:navy;
text-align:center }
tr {width:40%;}
tr:nth-child(odd) {background: aqua;}
tr:nth-child(even) {background: azure;}	
</style>
<body>
<h1>ACE Interface Guide</h1>
"""
#Dictionary of Properties
MGM_Properties = {"Aria" : "V20WDADVSQL01P",
    "Beau Rivage" : "V21WDADVSQL01P",
    "Bellagio" : "V22WDADVSQL01P",
    "Borgata" : "V41WDADVSQL01P",
    #"Cosmopolitan":"TBD",
    "Detroit" : "V31WDADVSQL01P",
    #"Empire" : "V43WDADVSQL01P",
    "Excalibur":"V27WDADVSQL01P",
    "Gold Strike" : "V38WDADVSQL01P",
    "Luxor" : "V28WDADVSQL01P",
    "Mandalay Bay":"V29WDADVSQL01P",        
    "MGM Las Vegas" : "V35WDADVSQL01P",
    "Mirage" : "V36WDADVSQL01P",
    "National Harbor" : "V33WDADVSQL01P",
    "New York, NY" : "V37WDADVSQL01P",
    "Northfield Park" : "V44WDADVSQL01P",
    "Park MGM" : "V40WDADVSQL01P",
    "Springfield" : "V34WDADVSQL01P",
    #"V'Dara" : "V39WDADVSQL01P" 
    }
for (MGM_Property,Server) in MGM_Properties.items():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + Server + ';'
                          'Database=playertracking;'
                          'Trusted_Connection=yes;')
    query = """select InterfaceName,InterfaceType,ServerName 
    from Interface (nolock) 
    where status = 'A' 
    order by InterfaceName"""
    
    #query = """	SELECT PlayerManagement.dbo.fn_GiftPointBalance(12345678, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) AS 'Gift Points'"""
    
    
        
    df = pd.read_sql_query(query, conn)
    htmlout +="<div><h2>" + MGM_Property + "</h2>"
    htmlout += df.to_html(classes='table table-stripped')
    htmlout += "</div>"
    print(htmlout)


htmlout += '<p>Last update: ' + filedate +"</body>"
ACEConnections = open(r"C:\Users\jgoeken\OneDrive - MGM Resorts International\Documents\~Temp\ACE_Connections.html","w")
ACEConnections.write(htmlout)
ACEConnections.close()


"""
import smtplib
from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = 'Hello World'
msg['from'] = 'jgoeken@mgmresorts.com'
msg['to'] = 'jgoeken@wgu.edu'
msg.set_ ('<h1>Hello World!!!</h1>')
smtp = smtplib.SMTP('exchange.mgmresorts.com:25')
smtp.send_message(msg)
smtp.quit()





"""