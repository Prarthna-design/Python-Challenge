import os
import csv

#create path for the filename
output_csv = os.path.join("Resources", "budget_data.csv")

print('Financial Analysis')

#open file, read and print header

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csvheader = next(csv_file)
    print(f'Header: {csvheader}')

    # total number of months included in the dataset
    next(csvreader)
    months = len(list(csvreader))
    print(f'Total Months: {months}')


    #The net total amount of "Profit/Losses" over the entire period

    







