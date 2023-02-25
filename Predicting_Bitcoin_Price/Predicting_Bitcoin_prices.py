'''
Goal of project: Prediction of Bitcoin Price
1. Import Api for Bitcoin (Done)
2. Get the current Price of Bitcoin (Done)
3. Predict the next month bitcoin price
4. And make a plot

Tools that may be needed
1. Requests
2. Pandas
3. Sclearn
4. Matplotlib
'''
import pandas as pd
import numpy as np
import requests
import requests
import json
from datetime import datetime

#Api for BitCoin Price from Coindesk.com
bitcoin_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Checking the connection (if connection is good, then it will give "200")
respons = requests.get(bitcoin_url)

def responsa_url():
    data = json.loads(respons.text) #Converts JSON string to dictionary.
    price = data['bpi']['USD']['rate'] #Extracts rate value of USD currency from bpi dictionary ny Elements/List
    print(price + ' USD')

def asking_the_user():
    asking = input('Do you want to predict the Bitcoin Price?  (Yes/No) ').lower()
    return asking

def predicting_the_bitcoin_price():
    # Predict and print out a vizulation


#Showing the Bitcoin price after a successful Connection
if respons.status_code == 200: # Using the Variable "respons" to check the link and thereafter run the loop
    responsa_url()
else:
    print('There is something wrong of the code')

answer = asking_the_user()

if answer == 'yes'





'''
Current Progress: 
Figure out how to show it nicely with price and date the code was runned 


Added to the Project
1. Add Date Time 
2. Use Statsmodel to predict the next day BitCoin Price




'''