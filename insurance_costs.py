import csv

insurance_records = []

with open('insurance.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        insurance_records.append(row)

def get_cost_and_count(records, comp_record, comp_crit_1, comp_crit_2):
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
male_total_cost, male_total_count, female_total_cost, female_total_count = get_cost_and_count(insurance_records, 'sex', 'male', 'female')

average_male_cost = male_total_cost / male_total_count
average_female_cost = female_total_cost / female_total_count

print(f"The average cost of insurance for males is: ${average_male_cost:.2f} and for females is: ${average_female_cost:.2f}")
print(f"{(male_total_count/len(insurance_records)*100):.2f}% of records are male and {(female_total_count/len(insurance_records)*100):.2f}% are female")

#This was an unexpected result as generally female insurance is more expensive
#2. Getting average cost for a smoker vs non-smoker

smoker_total_cost, smoker_total_count, non_smoker_total_cost, non_smoker_total_count = get_cost_and_count(insurance_records, 'smoker', 'yes', 'no')

average_smoker_cost = smoker_total_cost / smoker_total_count
average_non_smoker_cost = non_smoker_total_cost / non_smoker_total_count

print(f"The average cost of insurance for smokers is: ${average_smoker_cost:.2f} and for non_smokers is: ${average_non_smoker_cost:.2f}")
print(f"{(smoker_total_count/len(insurance_records)*100):.2f}% of records are smokers and {(non_smoker_total_count/len(insurance_records)*100):.2f}% are non-smokers")

#3. Are there more male than female smokers? This would drive up the average
male_smoker_count = 0
female_smoker_count = 0

for record in insurance_records:
    if record["smoker"] == "yes":
        if record["sex"] == "male":
            male_smoker_count += 1
        elif record["sex"] == "female":
            female_smoker_count += 1

print(f"There are {male_smoker_count} male smokers which is {(male_smoker_count/male_total_count*100):.2f}% of all males in the set and {(male_smoker_count/len(insurance_records)*100):.2f}% of total sample.")
print(f"There are {female_smoker_count} female smokers which is {(female_smoker_count/female_total_count*100):.2f}% of all females in the set and {(female_smoker_count/len(insurance_records)*100):.2f}% of total sample.")
