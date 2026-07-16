import csv

students = []

with open("second_students.csv") as file:
    reader = csv.reader(file) #DictReader is safer and better
    for name, city in reader:
        students.append({"name": name, "city": city})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['city']}")