import os
import csv

csvpath = os.path.join('..', 'Polling_Script.py', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)













