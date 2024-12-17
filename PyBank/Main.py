
# Dependencies
import os
import csv


# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
months = []  # List to store months 
net_change_list = [] # List to store month-to-month net changes

# Open and read the csv
with open(file_to_load, mode='r') as file:
    reader = csv.reader(file)
 # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
     
    for row in reader:

        # Track the total
        total_months += 1
        
        # Track the net change
        total_net += int(row[1])
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        months.append(row[0])
        prev_net = int(row[1])

    # Calculate the greatest increase in profits (month and amount)
    greatest_increase_amt = max(net_change_list)
    greatest_increase_month = months[net_change_list.index(greatest_increase_amt)]  # +1 to align with month

    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease_amt = min(net_change_list)
    greatest_decrease_month = months[net_change_list.index(greatest_decrease_amt)]  # +1 to align with month

    # Step 6: Calculate the average net change
    average_net_change = sum(net_change_list) / len(net_change_list) if len(net_change_list) > 0 else 0

    # Step 7: Display results

    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_net_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amt})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amt})\n"
    )
    
    # Print the output
    print(output)
    
    # Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)