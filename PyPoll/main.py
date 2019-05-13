# Dependencies
import os
import csv

# Specify the file to write to
election_path = os.path.join("..", "Resources", "election_data.csv")

Total_Votes = 0
candidates = []
votes_percent = []

# List to track pie purchases
pie_purchases = []

with open(election_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(csv_header)

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def vote_percentages(csvreader):
    # For readability, it can help to assign your values to variables with descriptive names
    name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

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

Avg_Change = change/Total_Months

#print(Total)
#print(Total_Months)
#print(Avg_Change)

#print(Greatest_Inc_month)
#print(Greatest_Inc)

#print(Greatest_Dec_month)
#print(Greatest_Dec)


# Output a summary of the analysis we just performed
#import sys
#sys.stdout = open('PyBank_Solution.txt','wt')

# Print Financial Analysis
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${Avg_Change}")
print(f"Greatest Increase in Profits: {Greatest_Inc_month} (${Greatest_Inc})")
print(f"Greatest Decrease in Profits: {Greatest_Dec_month} (${Greatest_Dec})")


# With an f-string, print out the daily wage that was calculated
#print(f"You make {daily_wage} per day") 'Greatest_Inc_month'
#print(f"DRAW PERCENT: {str(draw_percent)}")
#print(f"{wrestler_data[0]} is a {type_of_wrestler}")

def listInformation(simpleList):
    print(f"The values within the list are...")
    for value in simpleList:
        print(value)
    print(f"The length of this list is... {len(simpleList)}")

#percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)

# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))