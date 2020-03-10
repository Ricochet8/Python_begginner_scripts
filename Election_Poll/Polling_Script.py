import os
import csv

from csv import DictReader

csvpath = os.path.join('election_data.csv')

def print_count(election_data):
    voter_id = str(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

    total_votes = election_data.voter_id.count()
    

    print('str{}'.format(total_votes))


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

  #  print(csvreader)

    header = next(csvreader)
    
    for row in csvreader:
        print(print_count)

   






khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0















