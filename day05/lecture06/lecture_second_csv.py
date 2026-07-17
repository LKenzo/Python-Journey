import csv

students = []

with open("second_students.csv") as file:
    reader = csv.DictReader(file) #DictReader is safer and better
    for row in reader:
        students.append({"name": row["name"], "city": row["city"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['city']}")