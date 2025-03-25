import sys
import pandas as pd
import matplotlib.pyplot as plt

#load datasets
electric = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Electric%20billing%20data.csv')
water = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Water%20billing%20data.csv')
natural_gas = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Natural%20Gas%20billing%20data.csv')
spending_trends = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Commodity%20Spending%20Trend.csv')

#fake data to be replaced when the user chooses a dataset to see a report of
chosen_data = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/blank.csv')
report_header = 'Choose a report'

def drawline(str):
    var = len(str)
    for i in range(0, var):
        sys.stdout.write('-')
    print('\n')

#display options
print('Select which data you would like to see:')
def showoptions():
    print('Press (1) for electric billing data')
    print('Press (2) for water billing data')
    print('Press (3) for natural gas billing data')
    print('Press (4) to see a report on spending trends over the past 12 months')

showoptions()
user_option = input('Select: ')          

#select data to view
while True:
    if user_option == '1':
        chosen_data = electric
        report_header = "Electric billing data since January 2022"
        break
    elif user_option == '2':
        chosen_data = water
        report_header = "Water billing data since January 2023"
        break
    elif user_option == '3':
        chosen_data = natural_gas
        report_header = "Natural Gas billing data since January 2022"
        break
    elif user_option == '4':
        chosen_data = spending_trends
        report_header = "Utility Spending Trends Over the Past 12 months"
        break
    else:
        showoptions()
        user_option = input('Please choose a valid option:')

#data cleaning

#monthly spending
print(report_header)
drawline(report_header)
print(chosen_data)
drawline(report_header)

#yearly avg
#line chart
plt.title(report_header)