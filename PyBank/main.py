# Import os module to create file path

import os

# Import csv to read csv file

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    total_months = 0
    profit_losses = 0
    change = 0
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0 

    csv_header = next(csvreader)
    for row in csvreader:
        total_months = total_months + 1
        profit_losses = profit_losses + int(row[1])
        
        if total_months != 1 :
            change = int(row[1]) - int(previous_row[1])
        total_change = total_change + change
        if greatest_increase < change:
            greatest_increase = change
            greatest_increase_month = row[0]
        if greatest_decrease > change:
            greatest_decrease = change
            greatest_decrease_month = row[0]
        previous_row = row

print("Financial Analysis\n----------------------------")

print(f'Total Months: {total_months}')
print(f"Total: {profit_losses}")
print(f'Average Change: {"{0:0.2f}".format(total_change/(total_months-1))}')      
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

# Specify the file to write to
output_path = os.path.join("analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.writelines("Financial Analysis\n----------------------------")

    txtfile.writelines(f'\nTotal Months: {total_months}')
    txtfile.writelines(f"\nTotal: {profit_losses}")
    txtfile.writelines(f'\nAverage Change: {"{0:0.2f}".format(total_change/(total_months-1))}')      
    txtfile.writelines(f'\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    txtfile.writelines(f'\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    txtfile.close()

   