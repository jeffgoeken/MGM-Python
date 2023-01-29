import pyodbc
import pandas as pd
from datetime import datetime
import logging
import  JeffsPyLibrary as jpl
import os

timestamp = (datetime.now()).strftime("%Y-%m-%d %H%M%S")
logfilepath = (rf"D:\Logs\SQLErr{timestamp}.log")

#create and configure the logger

logging.basicConfig(filename = logfilepath,format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def Main(ReportName,strStartDate,strEndDate,SiteID):
    timestamp = (datetime.now()).strftime("%Y-%m-%d %H%M%S")
    filepath = (rf"D:\Loyalty_Scripts\Loyalty Reports\Finished\Bonus Adjustment by Adjustor {timestamp}.xlsx")

    #filepath = (rf"D:\Loyalty Archive\Bonus Adjustment by Adjustor for daterange {strStartDate} - {strEndDate} ran on {timestamp}.xlsx")
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                      #'Server=s1playrpt03p;'
                      'Server=playdb01r;'
                      'Database=playermanagement;'
                      'Trusted_Connection=yes;')

        logger.info("Connection Successful")

    except pyodbc.Error as err:
        logger.exception("Connection Failed")
        print(err)
    query = (f"exec {ReportName} '{strStartDate}','{strEndDate}' ,null,null,{SiteID}")

    df = pd.read_sql_query(query, conn)
    logger.info("SQL Query Successful")


    print(df)
    
    df1= df.loc[:1048573]
    df2 = df.loc[1048574:2097147]
    df3 = df.loc[2097148:3145721]
    df4 = df.loc[3145722:4194295]
    df5 = df.loc[4194296:5242869]
    df6 = df.loc[5242870:6291433]



    with pd.ExcelWriter(filepath) as writer:
        df1.to_excel(writer, sheet_name= 'Sheet 1')
        df2.to_excel(writer, sheet_name= 'Sheet 2')
        df3.to_excel(writer, sheet_name= 'Sheet 3')
        df4.to_excel(writer, sheet_name= 'Sheet 4')
        df5.to_excel(writer, sheet_name= 'Sheet 5')
        df6.to_excel(writer, sheet_name= 'Sheet 6')
                     

def Initialize():
    files = os.listdir('D:\\Loyalty_Scripts\\Loyalty Reports\\Qued')
    for file in files:

        openFilePath = (f'D:\\Loyalty_Scripts\\Loyalty Reports\\Qued\\{file}')
        archiveFilePath = (f'D:\\Loyalty_Scripts\\Loyalty Reports\\Archived\\{file}')
        finishedReports = "D:\Loyalty_Scripts\Loyalty Reports\Finished"
        reports = jpl.GetDataFromExcel(openFilePath,archiveFilePath)
        for index, row in reports.iterrows():
            ReportName,StartDate,EndDate,SiteID =  row

            Main(ReportName,StartDate,EndDate,SiteID)
                 

Initialize()
"""
Periods = {
('10-01-2022','10-15-2022'),
('10-16-2022','10-31-2022'),
('11-01-2022','11-15-2022'),
('11-16-2022','11-30-2022'),
('12-01-2022','12-15-2022'),
('12-16-2022','12-31-2022')

}
for Period in Periods:
    startd,endd = month
    print(f"Start date is {startd} and end date is {endd}")
    Main(startd,endd,24)
"""




#Main('2022-12-01','2022-12-31',24)


"""
SiteID	Description
1	Mirage
2	Treasure Island
3	MGM Grand
4	New York New York
5	MGM Detroit
6	Bellagio
7	Borgata Pre-Conversion
8	Beau Rivage
9	Mandalay Bay
10	Park MGM
11	Luxor
12	Excalibur
13	Circus Circus Las Vegas
14	Gold Strike
15	BetMGM
16	ARIA
17	Vdara
18	MGM National Harbor
19	Borgata
20	MGM Springfield
24	MGM Northfield Park
25	Empire City Casino
"""
