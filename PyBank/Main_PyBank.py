import os
import csv
import numpy as np

path = os.path.join("Resources","budget_data.csv")

with open(path) as budget:
    csvreader = csv.reader(budget,delimiter = ",")
    
    header = next(csvreader)

    row1 = next(csvreader)

    month = 1
    total = int(row1[1])

    last_value = int(row1[1])

    change = []
    months = []

    for row in csvreader:
        if months != 0:
            change.append(int(row[1]) - int(last_value))
            months.append(row[0])
            last_value = int(row[1])

        month +=1
        total = int(row[1]) + total

    d = dict(zip(change, months))

    print(f'Financial Analysis')
    print(f'---------------------------')
    print(f'Total Months : {month}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(np.mean(change),2)}')
    print(f'Greatest Increase in Profits: {d.get(np.max(change))} (${np.max(change)})')
    print(f'Greatest Decrease in Profits: {d.get(np.min(change))} (${np.min(change)})') 