import requests
import pyodbc 

server = 'tcp:thm-sqlserver.database.windows.net'
database = 'dev'
username = 'sqluser'
password = 'sql@12345'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

URL = "https://rest.netsuite.com/app/site/hosting/restlet.nl"

querystring = {"script":"364","deploy":"1"}

headers = {
    'authorization': "NLAuth nlauth_account=62886, nlauth_email=emily@punchbuggy.com.au, nlauth_signature=Access99",
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("GET", URL, headers=headers, params=querystring)

response_data = response.json()

for object in response_data:
    ItemCode = object['ItemCode']
    ItemDescription = object['ItemDescription']
    QtyOnHand = object['QtyOnHand']
    QtyCommitted = object['QtyCommitted']
    QtyAvailable = object['QtyAvailable']
    cursor = cnxn.cursor()
    SQLCommand="INSERT INTO dbo.response_data (ItemCode,ItemDescription,QtyOnHand,QtyCommitted,QtyAvailable) values(?,?,?,?,?)"		
    Values = [ItemCode,ItemDescription,QtyOnHand,QtyCommitted,QtyAvailable]  
    cursor.execute(SQLCommand,Values) 
    cnxn.commit() 	
	 
   
