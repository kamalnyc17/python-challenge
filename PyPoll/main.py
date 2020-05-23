# user defined function to write in file and display on terminal at the same time
def outputResults(fileName, data):
    print(data)
    fileName.write(data+"\n")

# importing modules
import os
import csv

# declaring top level variables
pollCSV, resultsFile = "./Resources/election_data.csv", "./analysis/results.txt"
resultsDictonary, totalVote, votePercentage = dict(), 0, 0

# opening the csv and creating reader object
with open(pollCSV, encoding='utf-8') as csvfile:
    poll_reader = csv.reader(csvfile)
    print("Processing Please Wait ")
    # skipping header and then looping through csv
    next(poll_reader)
    for row in poll_reader:
        candidate = row[2]
        totalVote += 1
        # creating/updating entry in dictonary
        if candidate in resultsDictonary:
            resultsDictonary[candidate] += 1
        else:
            resultsDictonary.update({candidate: 1})   

# clearing screen, opening analysis file and displaying & writing results through user defined function
os.system('cls' if os.name == 'nt' else 'clear')
outputFile = open(resultsFile, "w")

outputResults(outputFile, "Election Results")
outputResults(outputFile, "-------------------------")
outputResults(outputFile, "Total Votes: " + str(totalVote))
outputResults(outputFile, "-------------------------")

for key in resultsDictonary:
    votePercentage = round((resultsDictonary[key] / totalVote) * 100, 3)
    outputResults(outputFile, key + ":  " + str(votePercentage) + "% (" + str(resultsDictonary[key]) +")")

outputResults(outputFile, "-------------------------")
outputResults(outputFile, "Winner: " + max(resultsDictonary, key=resultsDictonary.get))
outputResults(outputFile, "-------------------------")

# closing results file
outputFile.close()

