import pandas as pd
import os
import shutil
import openpyxl

def GetDataFromTxt():
    openFilePath =""
    openFileName = ""

    txtContent = open(openFilePath + openFileName, "r")
    print(txtContent)
    return txtContent

def GetDataFromCSV():
    openFilePath = (r'D:\Loyalty_Scripts\Loyalty Reports\Qued\test.csv')
    openFileName = r'test.csv'
    archiveFilePath = (r'D:\Loyalty_Scripts\Loyalty Reports\Archived\test.csv')
    #archiveFilePath = copyFile(openFilePath,openFileName,archiveFilePath)
    excelContent = pd.read_csv(archiveFilePath,delimiter=',',index_col=None, header=0)
    return excelContent()

def GetDataFromExcel(quedFilePath,archiveFilePath):
    copyFile(quedFilePath,archiveFilePath)
    excelContent = pd.read_excel(archiveFilePath,index_col=None, header=0)
    return excelContent

def copyFile(quedFilePath,archiveFilePath):
    shutil.copy(quedFilePath,archiveFilePath)
    os.remove(quedFilePath)


