# import csv package                            [POINTS: 1]

import csv

# initialize variable(s) to store data          [POINTS: 2]

fields = []
rows = []

filename = "car_sales.csv"

# read file data                                [POINTS: 2]

with open(filename, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

# skip or save header                           [POINTS: 1]

    fields = next(csv_reader)

# save row's data to local variable             [POINTS: 2]

    for row in csv_reader:
        rows.append(row)

# conditional statements to filter data         [POINTS: 7]
# only females who have sales experience of less than 5 years

for i in rows:
    if i[3] == 'F' and int(i[4]) < 5:
        for col in i:
            print(col + "\t", end='')
        print()