import csv

with open('WeekSix_Mod_20/data/my_friends.csv','r') as file:
    lines = csv.reader(file)
    header = next(lines)
    for line in lines:
        print(line)
    print(header)