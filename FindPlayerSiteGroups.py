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


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Playdb01r;'
                      'Database=playermanagement;'
                      'Trusted_Connection=yes;')

GetPlayers = """select top 5 playerid from player (nolock) where Status = 'A' order by playerid desc"""

#query = """	SELECT PlayerManagement.dbo.fn_GiftPointBalance(12345678, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) AS 'Gift Points'"""

Players  = pd.read_sql_query(GetPlayers, conn)



#df.to_csv ((path.format(filedate)), index = False, header = True)

for player in Players.playerid:
    query = 'select count (playerid) as cnt from playersitegroup (nolock) where playerid = ' + str(player)
    SiteIDs = pd.read_sql_query(query, conn)
    print (SiteIDs)

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