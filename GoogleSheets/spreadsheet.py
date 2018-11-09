import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
COL = client.open("201920 SEVIS Registration").sheet1
transferUG = client.open("201920 SEVIS Registration").sheet2
transferGR = client.open("201920 SEVIS Registration").sheet3
new_students = client.open("201920 SEVIS Registration").sheet4
continuing_students = client.open("201920 SEVIS Registration").sheet5