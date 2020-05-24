#PyBank - Analyzing bank's financial performance
# user defined function to write in file and display on terminal at the same time
def outputResults(fileName, data):
    print(data)
    fileName.write(data+"\n")

# import modules
import os
import csv

# declaring top level variables
budgetCSV, resultsFile = "./Resources/budget_data.csv", "./analysis/results.txt"
totalMonths, netProfitLoss, monthlyAverageChange, greatestProfitIncrease, greatestLossDecrease = 0, 0, 0, 0, 0
monthGreatestProfitIncrease, monthGreatestLossDecrease = "", ""
monthName, monthlyProfitLoss = [], []

# opening the csv and creating reader object
with open(budgetCSV, encoding='utf-8') as csvfile:
    budgetReader = csv.reader(csvfile)
    print("Processing Please Wait ")
    # skipping header and then looping through csv to creating column array's
    next(budgetReader)
    for row in budgetReader:
        totalMonths += 1
        netProfitLoss += int(row[1])
        monthName.append(str(row[0]))
        monthlyProfitLoss.append(int(row[1]))

    # traversing through column array's to perform rest of the calculations
    previousMonth = monthlyProfitLoss[0]
    totalMonthlyChange = 0
    for x in range(1, len(monthlyProfitLoss)):
        monthlyChange = monthlyProfitLoss[x] - previousMonth
        previousMonth = monthlyProfitLoss[x]
        totalMonthlyChange += monthlyChange

        if (monthlyChange > greatestProfitIncrease):
            greatestProfitIncrease = monthlyChange
            monthGreatestProfitIncrease = monthName[x]
        if (monthlyChange < greatestLossDecrease):
            greatestLossDecrease = monthlyChange
            monthGreatestLossDecrease = monthName[x]

    monthlyAverageChange = round(totalMonthlyChange / (totalMonths-1), 2)
    
# clearing screen, opening analysis file and displaying & writing results through user defined function
os.system('cls' if os.name == 'nt' else 'clear')
outputFile = open(resultsFile, "w")

outputResults(outputFile, "Financial Analysis")
outputResults(outputFile, "-------------------------")
outputResults(outputFile, f'Total Months: {totalMonths}')
outputResults(outputFile, f'Total: {"${:,.0f}".format(netProfitLoss)}')
outputResults(outputFile, f'Average Change: {"${:,.2f}".format(monthlyAverageChange)}')
outputResults(outputFile, f'Greatest Increase in Profits: {monthGreatestProfitIncrease} ({"${:,.0f}".format(greatestProfitIncrease)})')
outputResults(outputFile, f'Greatest Decrease in Profits: {monthGreatestLossDecrease} ({"${:,.0f}".format(greatestLossDecrease)})')

# closing results file
outputFile.close()