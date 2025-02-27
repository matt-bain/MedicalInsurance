import csv

insurance_records = []

with open('insurance.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        insurance_records.append(row)

#1. find average cost of insurance for male vs female
#start with finding totals for each sex and the count
male_total_cost, male_total_count = 0, 0
female_total_cost, female_total_count = 0, 0

for record in insurance_records:
    if record['sex'] == "male":
        male_total_count += 1
        male_total_cost += float(record['charges'])
    elif record['sex'] == "female":
        female_total_count += 1
        female_total_cost += float(record['charges'])

average_male_cost = male_total_cost / male_total_count
average_female_cost = female_total_cost / female_total_count

print(f"The average cost of insurance for males is: ${average_male_cost:.2f} and for females is: ${average_female_cost:.2f}")


