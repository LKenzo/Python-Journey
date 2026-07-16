import csv

name = input("What's your name?")
home = input("What's your city?")

with open("second_student.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])