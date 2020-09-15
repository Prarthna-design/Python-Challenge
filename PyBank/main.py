import os
import csv

#create path for the filename
output_csv = os.path.join("Resources", "budget_data.csv")

# print header
print('Financial Analysis')

#open file, read and print header

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    

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
    
# need to find way to read the data in pair for data and amount
#nedd to calculate difference between each data points. 
#create new column? 
# identify the highest profit within new column
#identify the lowest loss within new column
#???????????????????????????????????????????

# Print the Analysis to the terminal 
# export a text file with the results.







