def main():
    grade = int(input("Input your score: "))
    check_grade(grade)

def check_grade(grade):
    if grade >= 80:
        print("Grade A")
    elif grade >= 70:
        print("Grade B")
    elif grade >= 60:
        print("Grade C")
    else:
        print("Grade D")

main()