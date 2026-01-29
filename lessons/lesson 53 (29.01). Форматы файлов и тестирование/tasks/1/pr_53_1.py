import csv

with open('students.csv', 'r', encoding='utf-8') as file:
   reader = csv.reader(file)

for row in reader:
    for subject in reader.fieldnames[1:]:
        try:
            grade = float(row[subject])
            subject_sums[subject] += grade
            subject_counts[subject] += 1
        averages = {}
        for subject in subject_sums:
            if subject_counts[subject] > 0:
                averages[subject] = subject_sums[subject] / subject_counts[subject]
        return averages

