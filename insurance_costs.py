import csv

insurance_list = []

with open('insurance.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        insurance_list.append(row)

