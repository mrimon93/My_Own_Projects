""" Road to Financial Freedom
This code will inform the user by asking the user:s desire goal of wealth and print out the money they have to earn per
day in order to accomplish their goals. It will be 2 part of the code.

--------------
1. Asking the user how much they want to earn and take the current date and calculate to the given date that the user
want to achieve the goal.
2. Asking More specific date like if they want to earn 1 Million dollar every year how much of day will it be etc.
--------------
1. Print out "Todays date" that the user are using this code
2. Asking the user the target goal
3. Asking what year they would like to achieve it
--------------
Other part of the code
-------------
1. Print the "Todays Date" when the user using the code
2. Asking the user for wealth goal
3. Print out the day that they have to earn every day to hit that target.
------
Lastly:
It will give the user option to print the data by using pandas as CSV file or Excel File
"""
import pandas as pd
import numpy as np
import calendar
import datetime
from datetime import date

today = date.today()
print('Hello my friend, Today is:', today, "\n")

def part_one_of_the_code():
    target_goal = float(input('What is your Money goal? (Write in numbers: '))
    target_date = input('What is the target date that you want to achieve the goal? ')
    sum_of_goal_date = target_date / target_date
    print('To achieve ', target_goal, ' on the date: ', target_date,'\n')
    print('You have to earn', sum_of_goal_date,'/Daily')

def part_two_of_the_code():
    pass

def printing_out_data():
    #If this part is chosen, then the code will use pandas in order to print out the data in to CSV and EXCEL file
    pass


