''' Goal: Update how many job you have applied for every week and every month
1. Update with Week and Month (Done)
2. Asking the User how many applicants
3. Ask them to write down the information (optional)
4. Print out the total (Example if you have applied 10 job every week for 2 Month you should get 80 application)
5. Get A grisp about how many percent you should have to get a job ( how is the ratio of getting a job)
6. Print out in Excel and CSV file

'''
import pandas as pd
import numpy as np
import calendar
from datetime import date


today = date.today()
print('Today is', today)

def calculate_weeks_in_month(year,month,day):
    #Define range for valid numbers in day and month
    valid_months = range(1,13)
    valid_days = range(1,32)

    #Validate input
    if month not in valid_months:
       raise ValueError('Invalid month, enter correct numbers')
    if day not in valid_days:
       raise ValueError('Invalid days, enter the correct numbers')


    #Calculate the number of the weeks in the choosen month
    cal = calendar.monthcalendar(year,month)
    num_weeks = len(cal)

    # Print the number of weeks
    print(f"There are {num_weeks} weeks in the month of {calendar.month_name[month]}, {year}.")
    return num_weeks

def asking_the_user_application():
    pass

def percent_ratio():
    print('Here you should get a ratio of your chance getting a job \n')

    pass



#Ask the user for year, month  and date
year = int(input('Enter the Year: '))
month = int(input('Enter the Month (1-12): '))
day = int(input('Enter the date (1-31) : '))


calculate_weeks_in_month(year, month, day)










'''
Things i have learned: 
----------------------------------------------------------------------------------------------------
About raise ValueError (From ChatGPT) (1 Mars 2023)
The raise statement in Python is used to raise an exception
hich is a signal that an error or exceptional condition has occurred 
during the execution of the program.

From (https://rollbar.com/blog/python-valueerror/)  (1 Mars 2023)
The Python ValueError is raised when the wrong value is assigned to an object.
This can happen if the value is invalid for a given operation, or if the value does not exist
For example, if a negative integer is passed to a square root operation, a ValueError is raised.
----------------------------------------------------------------------------------------------------






'''