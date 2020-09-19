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
    header = next(csvreader)
    net = []
    months = []
    for row in csvreader: 
        net.append(float(row[1]))
        months.append(row[0])
        # print(type(row[1]))
# print(months)

print(f'Total: {sum(net)}')

# average of change in "Profit_Losses"
profitlosschange = []
for value in net[1:]:
    i = net[net.index(value) - 1]
    change = value - i
    profitlosschange.append(change)
# print(profitlosschange)


average = sum(profitlosschange) / len(profitlosschange)
  
print(f'Average Change: $ {str(round(average, 2))}')

GreatestIncrease = max(profitlosschange)
print(GreatestIncrease)
g = profitlosschange.index(GreatestIncrease) +1
maxmonth = months[g]
print(f'Greatest Increase in Profits: {maxmonth} ${str(GreatestIncrease)}')

GreatestDecrease = min(profitlosschange)
# print(GreatestDecrease)
d = profitlosschange.index(GreatestDecrease) +1
minmonth = months[d]
# print(minmonth)



#     # the greatest increase in profits (date and ampunt) 
#     # #over the entire period
# with open(output_csv) as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=',')
    
# # need to find way to read the data in pair for data and amount
# #nedd to calculate difference between each data points. 
# #create new column? 
# # identify the highest profit within new column
# #identify the lowest loss within new column
# #???????????????????????????????????????????

# # Print the Analysis to the terminal 
# # export a text file with the results.







