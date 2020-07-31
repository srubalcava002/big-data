import csv
import sys
import os
import glob

directory = '/home/user/Documents/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us'
list = []
files = os.listdir(directory)
flag = True
i = 0

# iterate through files in directory
for file in files:
    if file.endswith('.csv'):   # check if the file is a csv
        with open(directory + '/' + file, 'r') as data:    # check if the file is a csv
            reader = csv.reader(data)
            line = [r for r in reader]
        if flag:    # writes the first line from the first file (fields)
            list.append(line[0])
            for l in line:      # prints each province and queries one to output aggregate data from
                print(str(i) + ' ' + l[0])
                i += 1
            query = input('Query: ')
            flag = False
        if file == '04-12-2020.csv':    # there is a discrepancy in 04-12-2020.csv
            if int(query) > 42:
                list.append(line[int(query) - 2])
            else:
                list.append(line[int(query) - 1])
            continue
        list.append(line[int(query)])    # add queried line of all csv files to list[]

output = directory + '/' + list[1][0] + '.csv'
with open(output, 'w') as out:      # write each line of list[] to output
    writer = csv.writer(out)
    for data in list:
        writer.writerow(data)

print('Wrote to ' + output)
