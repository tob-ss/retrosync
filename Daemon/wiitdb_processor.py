# create second python script; for ech line, extract first 6 characters. then skip the next three (as they are space and =) then add the rest as a value to the key which is the first 6 characters
# make that a csv

#with open('wiitdb.txt', 'r') as file:
#     data = file.read()
#     print(data)
#     x = 0
#     while x <= 5:
#        for line in data:
#            print(line)
#            x += 1

import csv

wiitdb_csv = []

file = open("wiitdb.txt")
for line in file:
    gameID = line[0:4]
    gameName = line[9:]
    wiitdb_csv.append({"Game ID": gameID, "Game Name": gameName})

wiitdb_csv_name = "csv/wiitdb_processed.csv"

fieldnames = ["Game ID", "Game Name"]

with open(wiitdb_csv_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(wiitdb_csv)
print(wiitdb_csv)