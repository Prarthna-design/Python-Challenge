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

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    net = []
    for row in csvreader: 
        net.append(int(row[1]))
    

    print(f'Total: {sum(net[1])}')
#trying to solve ValueError for line 29
    val = "10.10"
    if val.isdigit():
        print(int(val))
# average of change in "Profit/Losses"

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    profit/loss = []
    average = sum(profit/loss) / len(profit/loss)
  
    print(f'Average Change: {str(round(average, 2)}')


    # the greatest increase in profits (date and ampunt) 
    # #over the entire period
with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    







