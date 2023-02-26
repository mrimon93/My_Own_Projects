'''
Goal of project: Prediction of Bitcoin Price
1. Import Api for Bitcoin (Done)
2. Get the current Price of Bitcoin (Done)
3. Predict the Day bitcoin price (Done)

Tools that may be needed
1. Requests
2. Pandas
3. Sclearn
5. Arima
'''
import pandas as pd
import numpy as np
import requests
import requests
import json
import datetime
from statsmodels.tsa.arima.model import ARIMA # New one for myself [26 Feb 2023]


#Api for BitCoin Price from Coindesk.com
bitcoin_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Checking the connection (if connection is good, then it will give "200")
respons = requests.get(bitcoin_url)

def responsa_url():
    data = json.loads(respons.text) #Converts JSON string to dictionary.
    price = data['bpi']['USD']['rate'] #Extracts rate value of USD currency from bpi dictionary ny Elements/List
    print('The Bitcoin Price is: ', price + ' USD')

def asking_the_user():
    asking = input('Do you want to predict the Bitcoin Price?  (Yes/No) ').lower()
    return asking

# Predicting the file with ARIMA MODEL
def predicting_the_bitcoin_price():
    #Loading the Bitcoin data
    today = datetime.date.today()
    predict_bitcoin_url = f'https://api.coindesk.com/v1/bpi/historical/close.json?start=2022-01-01&end={today}'
    response = requests.get(predict_bitcoin_url)
    data = response.json()
    df = pd.DataFrame.from_dict(data['bpi'],orient='index', columns=['price'])
    return df

def Arima_Model():
    model =ARIMA(predicting_the_bitcoin_price(), order=(2,1,0))# ARIMA(p,d,q) with p=2, d=1, q=0
    model_fit = model.fit()
    # make predictions for next day
    next_day = pd.date_range(start='2022-03-01', end='2022-03-01', freq='D')
    forecast = model_fit.forecast(steps=1)
    print('The Predicted Price of BitCoin is: ' ,forecast)


#Showing the Bitcoin price after a successful Connection
if respons.status_code == 200: # Using the Variable "respons" to check the link and thereafter run the loop
    responsa_url()
else:
    print('There is something wrong of the code')

answer = asking_the_user()

if answer == 'yes':
    Arima_Model()
else:
    print('Yep You Suck')


print('That is the end of the code')




'''
Current Progress: 
Figure out how to show it nicely with price and date the code was runned 

Added to the Project
1. Add Date Time 
2. Use Statsmodel to predict the next day BitCoin Price
3.

'''
