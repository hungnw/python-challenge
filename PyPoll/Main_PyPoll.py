import csv
import os

path = os.path.join("Resources", "election_data.csv")

with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    candidates = []
    votes = []
    vote_percent = []
    
    total_votes = 0

    winner = ""
        
    next(csvreader, None)
    for row in csvreader:
        if row[-1] not in candidates:
            candidates.append(row[-1])
            votes.append(1)
        else:
            index = candidates.index(row[-1])
            votes[index] += 1
        total_votes += 1
    
    for v in votes:
        percent = "{0:.3f}".format(round((v/total_votes)*100, 2))
        vote_percent.append(percent) 
        
    winner_index = vote_percent.index(max(vote_percent))
    winner = candidates[winner_index]
            

    print('Election Results')
    print('-------------------------')
    print(f'Total votes: {total_votes}')
    print('-------------------------')
    print(f'{candidates[0]} : {vote_percent[0]} % ({votes[0]})')
    print(f'{candidates[1]} : {vote_percent[1]} % ({votes[1]})')
    print(f'{candidates[2]} : {vote_percent[2]} % ({votes[2]})')
    print(f'{candidates[3]} : {vote_percent[3]} % ({votes[3]})')
    print('-------------------------')
    print(f'Winner: {winner}')

txt = open('election_results.txt', 'w')

txt.write('Election Results')
txt.write("\n")
txt.write('-------------------------')
txt.write("\n")
txt.write('Total votes: {total_votes}')
txt.write("\n")
txt.write('-------------------------')
txt.write("\n")
txt.write(f'{candidates[0]} : {vote_percent[0]} % ({votes[0]})')
txt.write("\n")
txt.write(f'{candidates[1]} : {vote_percent[1]} % ({votes[1]})')
txt.write("\n")
txt.write(f'{candidates[2]} : {vote_percent[2]} % ({votes[2]})')
txt.write("\n")
txt.write(f'{candidates[3]} : {vote_percent[3]} % ({votes[3]})')
txt.write("\n")
txt.write('-------------------------')
txt.write("\n")
txt.write(f'Winner: {winner}')

txt.close()



