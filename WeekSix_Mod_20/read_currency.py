import csv

moneyUsd = 50
moneyTaka = 5000

with open("WeekSix_Mod_20/data/currencyrates.csv","r") as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(f"50 USD to BDT: {float(line[3])*moneyUsd}")
            print(f"5000 BDT to USD: {moneyTaka/float(line[3])}")




# Home Work
# convert 50 USD to BDT
# convert 5000 BDT to USD