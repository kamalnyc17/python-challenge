# importing modules
import os
import csv

# declaring top level variables
poll_csv = "./Resources/election_data.csv"
results_txt = "./analysis/results.txt"
results = {}

# opening the csv and creating reader object
with open(poll_csv, encoding='utf-8') as csvfile:
    poll_reader = csv.reader(csvfile)

    # looping through csv
    i = 0
    for row in poll_reader:
        candidate = row[2]
        # creating/updating entry indictonary

        print(candidate)
        i += 1
        if i > 100:
            break
