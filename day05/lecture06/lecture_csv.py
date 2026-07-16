students = []

with open("students.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['city']}")