import csv

name = input("What's your name? ")
city = input("What's your city? ")

with open("input_student.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, city])
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city}) 