# importing modules
import os
import csv

# declaring top level variables
poll_csv = "./Resources/election_data.csv"
results_txt = "./analysis/results.txt"
results_dict = dict()
totalVote = 0
votePercentage = 0
theWinner = ""

# opening the csv and creating reader object
with open(poll_csv, encoding='utf-8') as csvfile:
    poll_reader = csv.reader(csvfile)
    print("Processing Please Wait ")
    # skipping header and then looping through csv
    next(poll_reader)
    for row in poll_reader:
        candidate = row[2]
        totalVote += 1
        # creating/updating entry indictonary
        if candidate in results_dict:
            results_dict[candidate] += 1
        else:
            results_dict.update({candidate: 1})

# clear screen and display result on terminal
os.system('cls' if os.name == 'nt' else 'clear')
print("Election Results")
print("----------------")
print(f"Total Votes: {totalVote}")
print("----------------")

for key in results_dict:
    votePercentage = round((results_dict[key] / totalVote) * 100, 3)
    print(f"{key}: {votePercentage: .3f}% ({results_dict[key]})")

theWinner = max(results_dict, key=results_dict.get)
print("----------------")
print(f"Winner: {theWinner}")
print("----------------")
