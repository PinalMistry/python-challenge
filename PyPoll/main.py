#PyPoll
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

#Module for reading CSV file
import csv

#Name the .csv file path
csvpath = os.path.join('election_data.csv')
#output path for text file
output_path = ('election_result.txt')

#Declare variables 
total_votes = 0
winner = ''
Winner_total_votes = 0

# Declare dictionary to store total vots per candidates
candidates = {}

#Open the .csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader) 

    for row in list(csvreader)[1:]:
        #count the total number of votes
        total_votes += 1

        if (row[2] in candidates):
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
        

#Print all of the results
print("Election Results")
print("----------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------------------------")
for key in list(candidates):
        candidates_percentage = (((candidates[key])*100)/total_votes)
        #print(candidates_percentage)
        print(key + ': ' + ("{:.3f}%".format(candidates_percentage)) + '   (' + str(candidates[key]) +')')
        if Winner_total_votes < candidates[key]:
             Winner_total_votes = candidates[key]
             winner = key
print("----------------------------------------------------------")
print(f"Winner: {winner}") 
print("----------------------------------------------------------")


#Output the results into a new text file
with open(output_path, 'w') as textfile:
    
    textfile.write("Election Results\n")
    textfile.write("------------------------------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("------------------------------------------------------\n")
    for key in list(candidates):
        candidates_percentage = (((candidates[key])*100)/total_votes)
        textfile.write(key + ': ' + ("{:.3f}%".format(candidates_percentage)) + '   (' + str(candidates[key]) +')\n')
    textfile.write("------------------------------------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("------------------------------------------------------\n")