# Import os module to create file path

import os

# Import csv to read csv file

import csv


csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    total_votes = 0
    candidates = []
    vote_analysis = []

    csv_header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
csvfile.close()

# creating dictionary and appending it to vote_analysis
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for candidate in candidates:
        
        votes = 0
        dict = {}
        for line in csvreader:
            if candidate == line[2]:
                votes = votes + 1
        dict["candidate"] = candidate
        dict["votes"] = votes            
        vote_analysis.append(dict)
        csvfile.seek(0)
csvfile.close()

# Specify the file to write to
output_path = os.path.join("analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.writelines(f"Election Results\n-------------------------\nTotal Votes: {total_votes}")
    txtfile.writelines("\n-------------------------")
    
print(f"Election Results\n-------------------------\nTotal Votes: {total_votes}")
print("-------------------------")

# code to analyse and print results
max_votes = 0 
for analysis in vote_analysis:
    percent_vote = (analysis["votes"]/total_votes)*100

    if analysis["votes"] > max_votes:
        max_votes = analysis["votes"]
        winner = analysis["candidate"]

    print(f'{analysis["candidate"]} : {percent_vote:.3f}% ({analysis["votes"]})')
    with open(output_path, 'a') as txtfile:   
        txtfile.writelines(f'\n{analysis["candidate"]} : {percent_vote:.3f}% ({analysis["votes"]})')


print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

with open(output_path, 'a') as txtfile:
    txtfile.writelines("\n-------------------------")  
    txtfile.writelines("\nWinner: " + winner)
    txtfile.writelines("\n-------------------------") 
txtfile.close()