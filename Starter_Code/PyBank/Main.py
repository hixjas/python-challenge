
import pandas as pd
import os

#Open file from directory
os.chdir("PyBank/")
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

    print("Greatest Decrease in Profits: ", greatest_decrease['Date'],'(', greatest_decrease['Change'],')', file=f)

