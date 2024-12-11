
import pandas as pd
import os

os.chdir("PyBank/Resources")
df = pd.read_csv('budget_data.csv')


#The total number of months included in the dataset
print('Total Months: ',df['Date'].count())

#The net total amount of "Profit/Losses" over the entire period
print('Total: $', df['Profit/Losses'].sum())


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
df['Change'] = df['Profit/Losses'].diff()
#print(df)
print('Average Change: $', df['Change'].mean())

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = df.loc[df['Change'].idxmax()]

# Display the DataFrame and the month with the greatest increase
#print(df)
print("Greatest Increase in Profits:", greatest_increase['Date'],'(' ,greatest_increase['Change'],')')

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = df.loc[df['Change'].idxmin()]

print("Greatest Decrease in Profits: ", greatest_decrease['Date'],'(', greatest_decrease['Change'],')')
