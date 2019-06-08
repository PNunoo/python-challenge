# Dependencies
import os
import csv

# Specify the file to write to
budget_path = os.path.join("..", "Resources", "budget_data.csv")

Total_Months=0
Total=0
change = 0
Avg_Change=0
Greatest_Inc=0
Greatest_Dec=0
Greatest_Dec_month = ''
Greatest_Inc_month = ''



with open(budget_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(csv_header)

    for row in csvreader:
        #print(str(row[0]))
        Total_Months = Total_Months + 1
        print(Total_Months)

        Total = Total + float(row[1])
        print(Total)

        if Total_Months > 1:
            change = change + float(row[1]) - prev_value
        
            
        prev_value = float(row[1])

        if float(row[1]) > Greatest_Inc:
            Greatest_Inc = float(row[1])
            Greatest_Inc_month = row[0]

        if float(row[1]) < Greatest_Dec:
            Greatest_Dec = float(row[1])
            Greatest_Dec_month = row[0]

Avg_Change = change / Total_Months

#print(Total)
#print(Total_Months)
#print(Avg_Change)

#print(Greatest_Inc_month)
#print(Greatest_Inc)

#print(Greatest_Dec_month)
#print(Greatest_Dec)
#percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)

# Output a summary of the analysis we just performed
#import sys
#sys.stdout = open('PyBank_Solution.txt','wt')

# Print Financial Analysis
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${int(Total)}")
print(f"Average Change: ${round(Avg_Change,2)}")
print(f"Greatest Increase in Profits: {Greatest_Inc_month} (${int(Greatest_Inc)})")
print(f"Greatest Decrease in Profits: {Greatest_Dec_month} (${int(Greatest_Dec)})")
print("-------------------------------------------------")


# With an f-string, print out the daily wage that was calculated
#print(f"You make {daily_wage} per day") 'Greatest_Inc_month'
#print(f"DRAW PERCENT: {str(draw_percent)}")
#print(f"{wrestler_data[0]} is a {type_of_wrestler}")

