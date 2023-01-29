# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyodbc 
import pandas as pd
import datetime as dt
x = dt.datetime.now()
filedate = x.strftime("%m%d%y")
print(x)
print(filedate)
path = "C:\\Users\\jgoeken\\Documents\\Self-Limit report{}.csv"

print(path.format(filedate))

#Dictionary of Properties
MGM_Properties = {
    }

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=playdb01r;'
                      'Database=playermanagement;'
                      'Trusted_Connection=yes;')

#query = """select InterfaceName,ServerName from Interface (nolock) where status = 'A' order by InterfaceName"""

#query = """	SELECT PlayerManagement.dbo.fn_GiftPointBalance(12345678, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) AS 'Gift Points'"""

query = "select * from site"
    
df = pd.read_sql_query(query, conn)
htmlout = df.to_html(classes='table table-stripped')
print(htmlout)

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