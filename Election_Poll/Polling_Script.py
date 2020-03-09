import os
import csv

from csv import DictReader

csvpath = os.path.join('..', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

  #  print(csvreader)

    csv_header = next(csvreader)
    print("CSV Header: {}".format(csv_header))

  #  for row in csvreader:
  #     print(row)


with open (csvfile):
    VoterID = [row[0] for row in DictReader(csvfile)]
    print(VoterID)

khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0



# for person in csvfile[2]:
#     if person == 'Khan':
#         khan_count[person] += 1
    
# print('Khan Count: {}'.format(khan_count))











