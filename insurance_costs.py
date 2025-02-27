import csv

insurance_records = []

with open('insurance.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        insurance_records.append(row)

def get_total_and_count(records, comp_record, comp_crit_1, comp_crit_2):
    crit_1_total_cost, crit_1_total_count = 0, 0
    crit_2_total_cost, crit_2_total_count = 0, 0

    for record in records:
        if record[comp_record] == comp_crit_1:
            crit_1_total_count += 1
            crit_1_total_cost += float(record['charges'])
        elif record[comp_record] == comp_crit_2:
            crit_2_total_count += 1
            crit_2_total_cost += float(record['charges'])

    return crit_1_total_cost, crit_1_total_count, crit_2_total_cost, crit_2_total_count
#1. find average cost of insurance for male vs female
#start with finding totals for each sex and the count
male_total_cost, male_total_count, female_total_cost, female_total_count = get_total_and_count(insurance_records, 'sex', 'male', 'female')

average_male_cost = male_total_cost / male_total_count
average_female_cost = female_total_cost / female_total_count

print(f"The average cost of insurance for males is: ${average_male_cost:.2f} and for females is: ${average_female_cost:.2f}")
print(f"{(male_total_count/len(insurance_records)*100):.2f}% of records are male and {(female_total_count/len(insurance_records)*100):.2f}% are female")


