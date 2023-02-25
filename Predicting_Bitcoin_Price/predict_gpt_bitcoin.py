import pandas as pd
import requests
from statsmodels.tsa.arima.model import ARIMA

# load bitcoin price data
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2022-01-01&end=2022-02-28'
response = requests.get(url)
data = response.json()
df = pd.DataFrame.from_dict(data['bpi'], orient='index', columns=['price'])

# fit ARIMA model
model = ARIMA(df, order=(2, 1, 0)) # ARIMA(p,d,q) with p=2, d=1, q=0
model_fit = model.fit()

# make predictions for next day
next_day = pd.date_range(start='2022-03-01', end='2022-03-01', freq='D')
forecast = model_fit.forecast(steps=1)

# print forecasted price
print(forecast)
