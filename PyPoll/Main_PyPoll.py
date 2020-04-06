import os
import csv

path = os.path.join("Resources","election_data.csv")

with open(path) as file:
    csvreader = csv.reader(file)
    next(csvreader)

    total_votes_count = 0
    
    all_names_voted = []

    unique_names = []
    percents = []
    vote_count_by_candidate = []

    for row in csvreader:
        
        #Get total votes count
        total_votes_count +=1
    
        #List out unique candidate names:
        if row[2] not in unique_names:
            unique_names.append(row[2])

        #List out all names voted:
        all_names_voted.append(row[2])

    for i in unique_names:
        
        #List out total votes of each candidate:
        x = all_names_voted.count(i)
        vote_count_by_candidate.append(x)

        #List out each candidate's percentage of all votes:
        p = x / total_votes_count * 100
        percents.append(p)

    #Get the highest vote number:
    h = max(vote_count_by_candidate)

    #Get the index of the highest vote:
    i = vote_count_by_candidate.index(h)

    #Get the winner's name:
    winner = unique_names[i]

    print('Election Results')
    print('---------------------------------')
    print(f'Total Votes: {total_votes_count}')
    print('---------------------------------')

    for i in range(len(unique_names)):
        print(f'{unique_names[i]} {percents[i]:.3f}% ({vote_count_by_candidate[i]})')
    
    print('---------------------------------')
    print(f'Winner: {winner}')

#Export to txt file:
with open("Election Result.txt", "w") as text:
    text.write('Election Results')
    text.write('\n---------------------------------')
    text.write(f'\nTotal Votes: {total_votes_count}')
    text.write('\n---------------------------------')

    for i in range(len(unique_names)):
        text.write(f'\n{unique_names[i]} {percents[i]:.3f}% ({vote_count_by_candidate[i]})')
    
    text.write('\n---------------------------------')
    text.write(f'\nWinner: {winner}')
    text.write('\n---------------------------------')
