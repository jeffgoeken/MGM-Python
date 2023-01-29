import pyodbc 
import pandas as pd
import datetime as dt
import DatePYcker 
from datetime import datetime


date = DatePYcker.display_msg()
print(type(date))
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=playdb01p;'
                      'Database=MLifeCreditCard;'
                      'Trusted_Connection=yes;')

query =f"""
declare @dtPeriodStartDate as date
set  @dtPeriodStartDate ='{date}'
select
Insertdate,
BankFilename,
ErrorReason,
(select top 1 r2.description from s1playrpt03p.playermanagement.dbo.PlayerRestrictions as r with (nolock)
 join s1playrpt03p.playermanagement.dbo.restrictioncodes as r1 with (nolock) on r.restrictionmaskid = r1.restrictionmaskid
 join s1playrpt03p.playermanagement.dbo.[RestrictionTypes] as r2 with (nolock) on r1.Typeid = r2.typeid
 where r.playerid =x.rewardmemberid
) as 'BanType',
(select top 1 r1.description from s1playrpt03p.playermanagement.dbo.PlayerRestrictions as r with (nolock)
 join s1playrpt03p.playermanagement.dbo.restrictioncodes as r1 with (nolock) on r.restrictionmaskid = r1.restrictionmaskid
 where r.playerid =x.rewardmemberid
) as 'BanName',
(select top 1 r1.description from s1playrpt03p.playermanagement.dbo.PlayerRestrictions as r with (nolock)
 join s1playrpt03p.playermanagement.dbo.site as r1 with (nolock) on r.siteid = r1.siteid
 where r.playerid =x.rewardmemberid)  as SiteName,
Filetype,
AcquistionPromoCode,
AgentOrSubAgent,
Rewardmemberid,
FirstName,

LastName,

DOB,

ARN,

case when PreviousRecordIdentifier=0 then '' else PreviousRecordIdentifier end [Previous ARN Identifier],

RewardsOfferName as[Reward Type],

RewardsAmountSign as 'Rewards(+/-)',

Amount as'Reawards Earned',

AddressLine1,

AddressLine2,

City,

State,

ZIPCode,

PrimaryPhoneNumber,

Email,

ProcessedDate

--into #jeffstemp

from (SELECT fbc.ID

         , fbc.InputFileHeaderID

         , fbc.InputFileTrailerID

         , fbc.InputFilerRecordID

         , fbc.BankFileName

         , fbc.VersionNumber

         , fbc.FileType

         , fbc.ErrorReason

         , fbc.InsertDate

         , naf.RecordType

         , naf.ARN

         , naf.LastName

         , naf.FirstName

         , naf.MiddleInitial

         , naf.Prefix

         , naf.Suffix

         , NULL as RewardsOfferName

         , NULL as RewardsProgram

         , NULL AS RewardsEarnedDate

         , naf.AddressLine1

         , naf.AddressLine2

         , naf.City

         , naf.State

         , naf.ZIPCode

         , naf.PrimaryPhoneNumber

         , naf.RewardMemberID

         , naf.Email

         , naf.AcquistionPromoCode

         , naf.AgentOrSubAgent

         , naf.DOB

         , naf.StatusID

         , naf.ProcessedDate

    ,NULL as RewardsAmountSign

    ,NULL as Amount,

       header.periodstartdate,

       '' PreviousRecordIdentifier

       from MLifeCreditCard.dbo.Mlife_FBC_InputFileHeaders as  header  with (nolock)

    join MLifeCreditCard.dbo.Mlife_FBC_ErrorLog AS fbc with (nolock) on header.headerid = inputfileheaderid and header.filetype =101

    JOIN MLifeCreditCard.dbo.Mlife_FBC_naf_InputFileRecords as  naf with (nolock)  ON fbc.InputFilerRecordID = naf.ID and naf.headerid = header.headerid

    and substring(errorrecord, 21, 16) = naf.ARN

    WHERE naf.StatusID =2 and convert(date,header.periodstartdate) = @dtPeriodStartDate

   

    UNION ALL

   

    SELECT fbc.ID

         , fbc.InputFileHeaderID

         , fbc.InputFileTrailerID

         , fbc.InputFilerRecordID

         , fbc.BankFileName

         , fbc.VersionNumber

         , fbc.FileType

         , fbc.ErrorReason

         , fbc.InsertDate

         , amf.RecordType

         , amf.ARN

         , amf.LastName

         , amf.FirstName

         , amf.MiddleInitial

         , amf.Prefix

         , amf.Suffix

         , NULL as RewardsOfferName

         , NULL as RewardsProgram

         , NULL AS RewardsEarnedDate

         , amf.AddressLine1

         , amf.AddressLine2

         , amf.City

         , amf.State

         , amf.ZIPCode

         , amf.PrimaryPhoneNumber

         , amf.RewardMemberID

         , amf.Email

         , amf.AcquistionPromoCode

         , amf.AgentOrSubAgent

         , NULL AS DOB

           , amf.StatusID

         , amf.ProcessedDate

    ,NULL as RewardsAmountSign

    ,NULL as Amount

              ,header.periodstartdate,

              PreviousRecordIdentifier

       from MLifeCreditCard.dbo.Mlife_FBC_InputFileHeaders as  header  with (nolock)

    JOIN MLifeCreditCard.dbo.Mlife_FBC_ErrorLog AS fbc with (nolock) on header.headerid = inputfileheaderid and header.filetype =401

    JOIN MLifeCreditCard.dbo.Mlife_FBC_AMF_InputFileRecords as amf    ON fbc.InputFilerRecordID = amf.ID and amf.headerid = header.headerid

    and substring(errorrecord, 21, 16) = amf.ARN

    WHERE amf.StatusID =2 and convert(date,header.periodstartdate) = @dtPeriodStartDate
    UNION ALL
    SELECT fbc.ID

         , fbc.InputFileHeaderID

         , fbc.InputFileTrailerID

         , fbc.InputFilerRecordID

         , fbc.BankFileName
         , fbc.VersionNumber
         , fbc.FileType
         , fbc.ErrorReason
         , fbc.InsertDate 
         , rfc.RecordType
         , rfc.ARN
         , rfc.LastName
         , rfc.FirstName
         , rfc.MiddleInitial
         , rfc.Prefix
         , rfc.Suffix
         , NULL as RewardsOfferName
         , NULL as RewardsProgram
         , NULL AS RewardsEarnedDate
         , NULL AS AddressLine1
         , NULL as AddressLine2
         , NULL as City
         , NULL as State
         , NULL as ZIPCode
         , NULL as PrimaryPhoneNumber
         , rfc.RewardMemberID
         , NULL as Email
         , NULL as AcquistionPromoCode
         , NULL as AgentOrSubAgent
         , NULL as DOB
         , rfc.StatusID

         , rfc.ProcessedDate

    ,NULL as RewardsAmountSign

    ,NULL as Amount

              ,header.periodstartdate,

              ''PreviousRecordIdentifier

       from MLifeCreditCard.dbo.Mlife_FBC_InputFileHeaders as  header  with (nolock)

    join MLifeCreditCard.dbo.Mlife_FBC_ErrorLog AS fbc with (nolock) on headerid = fbc.inputfileheaderid and header.filetype = 131

    JOIN MLifeCreditCard.dbo.Mlife_FBC_RCF_InputFileRecords as rfc    ON fbc.InputFilerRecordID = rfc.ID and  rfc.headerid = header.headerid

    and substring(errorrecord, 21, 16) = rfc.ARN
    WHERE rfc.StatusID =2 and convert(date,header.periodstartdate) = @dtPeriodStartDate
    UNION ALL
    SELECT fbc.ID

         , fbc.InputFileHeaderID

         , fbc.InputFileTrailerID

         , fbc.InputFilerRecordID

         , fbc.BankFileName

         , fbc.VersionNumber

         , fbc.FileType

         , fbc.ErrorReason

         , fbc.InsertDate 

         , rpf.RecordType

         , rpf.ARN

         , rpf.LastName

         , rpf.FirstName

         , rpf.MiddleInitial

         , rpf.Prefix

         , rpf.Suffix

         --, rpf.RewardsAmountSign

         --, rpf.RewardsEarned

         , rpf.RewardsOfferName

         , rpf.RewardsProgram

         , rpf.RewardsEarnedDate

         , NULL as AddressLine1

         , NULL as AddressLine2

         , NULL as City

         , NULL as State

         , NULL as ZIPCode

         , NULL as PrimaryPhoneNumber

         , rpf.RewardMemberID

         , NULL as Email

         , NULL as AcquistionPromoCode

         , NULL as AgentOrSubAgent

         , NULL as DOB

          , rpf.StatusID

         , rpf.ProcessedDate

    ,rpf.RewardsAmountSign

    ,rpf.RewardsEarned as Amount

              ,header.periodstartdate,

              ''PreviousRecordIdentifier

       from MLifeCreditCard.dbo.Mlife_FBC_InputFileHeaders as  header  with (nolock)

    join MLifeCreditCard.dbo.Mlife_FBC_ErrorLog AS fbc with (nolock) on headerid = fbc.inputfileheaderid and header.filetype = 251

    JOIN MLifeCreditCard.dbo.Mlife_FBC_RPF_InputFileRecords as rpf  ON fbc.InputFilerRecordID = rpf.ID and  rpf.headerid = header.headerid

    and substring(errorrecord, 21, 16) = rpf.ARN

    WHERE rpf.StatusID =2 and convert(date,header.periodstartdate) = @dtPeriodStartDate

       )x

--     Left join

--SELECT statusid,HeaderID,PeriodStartDate,PeriodEndDate,InsertDate,FileName FROM dbo.Mlife_FBC_InputFileHeaders WHERE InsertDate >='12/01/2021' ORDER BY insertdate desc

----   SELECT * FROM dbo.Mlife_FBC_RPF_InputFileRecords WHERE RewardMemberID like '9542886356%' ORDER BY InsertDate desc

--     --SELECT * FROM  MLifeCreditCard.dbo.Mlife_FBC_RCF_InputFileRecords WHERE RewardMemberID='79375391' ORDER BY InsertDate desc

--        BEGIN TRAN

--UPDATE  dbo.Mlife_FBC_RPF_InputFileRecords

--SET RewardMemberID='9542886356'

 

--where id in (9507896,

--9507897)

------commit

 

--        BEGIN TRAN

--UPDATE dbo.Mlife_FBC_NAF_InputFileRecords

--SET RewardMemberID='9542886356'

 

--where id in (463454)

 --drop table #jeffstemp

------commit

--SELECT * FROM PlayerManagement.dbo.playername nolock WHERE lastname='FRANKEN'and firstname='COLLEEN'

--SELECT * FROM dbo.Mlife_FBC_NAF_InputFileRecords WHERE RewardMemberID like '96797943%' ORDER BY InsertDate desc


--select * from #jeffstemp
--where rewardmemberid = 73573017
"""

timestamp = (datetime.now()).strftime("%Y-%m-%d")
filename = (f"MLCC Exeption Report {timestamp}.xlsx")

df = pd.read_sql_query(query, conn)
print(df)
dfSum = df.pivot_table(index = ['ErrorReason'],aggfunc='size').sort_values(ascending=False)
print(dfSum)
df.to_excel(r'C:/Users/jgoeken/Downloads/test.xlsx')

with pd.ExcelWriter(rf'C:/Users/jgoeken/Downloads/{filename}') as writer:
        df.to_excel(writer, sheet_name='Data Sheet')
        dfSum.to_excel(writer, sheet_name='Pivot Sheet')
