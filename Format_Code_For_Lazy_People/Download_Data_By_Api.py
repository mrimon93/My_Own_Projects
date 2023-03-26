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



#Get the API key and then execute one of those
url = ""



# Getting the Response of the Link
response = requests.get(url)
print(response)
