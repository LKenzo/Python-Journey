def main():
    num1 = input_num("first")
    num2 = input_num("second") 

    calculator(num1, num2)

def input_num(prompt):
    while True:
        try:
            return int(input(f"Input the {prompt} number: "))
        except ValueError:
            print("Invalid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

def calculator(num1, num2):
    print(f"addition of {num1} + {num2}:", num1 + num2)
    print(f"substraction of {num1} - {num2}:", num1 - num2)
    print(f"multiplication of {num1} x {num2}:", num1 * num2)
    print(f"division of {num1} / {num2}:", num1 / num2)

main()