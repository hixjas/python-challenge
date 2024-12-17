
import pandas as pd
import os
import csv

#Open file from directory
""" os.chdir("PyBank/")
df = pd.read_csv('Resources/budget_data.csv')

#Create output file and path for summary results
file_to_output =  os.path.join("analysis", "budget_analysis.txt")

with open(file_to_output, 'a') as f:
   
#The total number of months included in the dataset
    print('Total Months: ',df['Date'].count(),file=f)

#The net total amount of "Profit/Losses" over the entire period
    print('Total: $', df['Profit/Losses'].sum(), file=f)


#The changes in "Profit/Losses" over time
    df['Change'] = df['Profit/Losses'].diff()
   
    #the average of those changes
    print('Average Change: $', df['Change'].mean(),file=f)

    #The greatest increase in profits (date and amount)
    greatest_increase = df.loc[df['Change'].idxmax()]

    # Display the DataFrame and the month with the greatest increase
    #print(df)
    print("Greatest Increase in Profits:", greatest_increase['Date'],'(' ,greatest_increase['Change'],')',file=f)

    #The greatest decrease in profits (date and amount) 
    greatest_decrease = df.loc[df['Change'].idxmin()]

    print("Greatest Decrease in Profits: ", greatest_decrease['Date'],'(', greatest_decrease['Change'],')', file=f) """

# Step 1: File path
file_to_load = os.path.join("Starter_Code","PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Step 2: Initialize variables
total_profit_loss = 0  # Total sum of Profit/Loss
profit_loss_values = []  # List to store Profit/Loss values
months = []  # List to store months
net_changes = []  # List to store month-to-month net changes

# Step 3: Read the CSV file
with open(file_to_load, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    # Read each row
    for row in csv_reader:
        month = row[0]
        profit_loss = int(row[1])  # Convert Profit/Loss to an integer
        months.append(month)  # Store the month
        profit_loss_values.append(profit_loss)  # Store the Profit/Loss
        total_profit_loss += profit_loss  # Add to total

# Step 4: Calculate month-to-month net changes
for i in range(1, len(profit_loss_values)):
    net_change = profit_loss_values[i] - profit_loss_values[i - 1]
    net_changes.append(net_change)

# Step 5: Find the highest increase and lowest decrease
greatest_increase_amt = max(net_changes)
greatest_increase_month = months[net_changes.index(highest_increase) + 1]  # +1 to align with month

greatest_decrease_amt = min(net_changes)
greatest_decrease_month = months[net_changes.index(lowest_decrease) + 1]  # +1 to align with month

# Step 6: Calculate the average net change
average_net_change = sum(net_changes) / len(net_changes) if len(net_changes) > 0 else 0

# Step 7: Display results

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(months)}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amt})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amt})\n"
)
print(output)