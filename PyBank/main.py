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

