#PyBank
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

#Module for reading CSV file
import csv

#Name the .csv file path
csvpath = os.path.join('budget_data.csv')
#output path for text file
output_path = ('budget_data_analysis.txt')

#Declare variables 
total_months = 0
total_Profit_Losses = 0
greatest_increase = 0
greatest_decrease = 0

# Lists to store data
profit_losses_list = []
change_list= []

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
     #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader) 
    
    for row in csvreader:
        #Add the total number of months
        total_months += 1
        #Add the profit/loss to the total amount
        profit_losses_list.append(float(row[1]))
        total_Profit_Losses += float(row[1])

        # Calculate the change in profit/losses from one month to the next
        if total_months > 1:
            change_list.append(profit_losses_list[-1] - profit_losses_list[-2])
        
        # Get the greatest increase and greatest decrease in profits
        if len(change_list) > 0:
            if change_list[-1] > greatest_increase:
                increase_period = row[0]
                greatest_increase = change_list[-1]
            elif change_list[-1] < greatest_decrease:
                decrease_period = row[0]
                greatest_decrease = change_list[-1]
    
    # Calculate the average change 
    average_change = sum(change_list) / len(change_list)

    #Print out all of the results
    print("Financial Analysis")
    print("------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total : ${total_Profit_Losses}")
    print(f"Average Change: ${format(average_change, '.2f')}")
    print(f"Greatest Increase in Profits: {increase_period} $({greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_period} $({greatest_decrease})")


#Output the results into a new text file
with open(output_path, 'w') as textfile:
    
    textfile.write("Financial Anlysis\n")
    textfile.write("------------------------------------------------------\n")
    textfile.write("Total Months: " + str(total_months) + "\n")
    textfile.write("Total : $" + str(total_Profit_Losses) + "\n")
    textfile.write("Average Change: $" + str(format(average_change, '.2f')) + "\n")
    textfile.write("Greatest Increase in Profits: " + increase_period + " $(" + str(greatest_increase) + ")\n")
    textfile.write("Greatest Decrease in Profits: " + decrease_period + " $(" + str(greatest_decrease) + ")\n")
