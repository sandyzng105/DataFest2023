import csv

with open('statesites.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    dict = {}
    for row in reader:
        if row[2] in dict:
            dict[row[2]] = dict[row[2]] + 1
        else:
            dict[row[2]] = 1
    with open('state_freq.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        #header
        writer.writerow(['StateName','Frequency'])
        for key in dict.keys():
            writer.writerow([key, dict[key]])