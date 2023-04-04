"""
1. Goal of the Code: Able to download information by API and thereafter able to download in:
- Pandas
- Json
-Excel
-Check The Connection (Good and Bad Response etc)

This Code will work as a format for future Codes

"""
import requests
import pandas as pd
import numpy as np

#Function Files
def Json_File():
    # Save To Json File
    name = input('Name of the file? ')
    df.to_json(name)
def CSV_File():
    # Save to CSV File
    name = input('Name of the file? ')
    df.to_csv(name, index=False)
def Excel_File():
    # Save to Excel File
    name = input('Name of the file? ')
    df.to_excel(name, index=False)


#Get the API key and then execute one of those
# An example: url = "https://api.publicapis.org/entries"

#Enter Your Api Key
url=""


# Getting the Response of the Link
response = requests.get(url)
print('The Response of the website is', response)

# Getting in to pandas

data = response.json()

df = pd.DataFrame(data)

print('Which file do you want to save in?')
print('Press 1 For Json-File')
print('Press 2 for CSV File')
print('Press 3 for Excel File')

choice = int(input('Choose your Number; '))

if choice == 1:
    Json_File()
elif choice == 2:
    CSV_File()
elif choice == 3:
    Excel_File()
else:
    print('You Suck! ')
