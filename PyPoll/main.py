# importing modules
import os
import csv

# declaring top level variables
poll_csv = "./Resources/election_data.csv"
results_txt = "./analysis/results.txt"
results_dict = dict()
totalVote = 0

# opening the csv and creating reader object
with open(poll_csv, encoding='utf-8') as csvfile:
    poll_reader = csv.reader(csvfile)
    # skipping header and then looping through csv
    next(poll_reader)
    i = 0
    for row in poll_reader:
        candidate = row[2]
        totalVote += 1
        # creating/updating entry indictonary
        if candidate in results_dict:
            results_dict[candidate] += 1
        else:
            results_dict.update({candidate: 0})

        print(row)
        i += 1
        if i > 1000:
            break

print(results_dict)
print(totalVote)
