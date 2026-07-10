def main():
    x = get_int
    # x = improved_get_int("Input the value of x: ")

    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("Input the value of x: "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        
# Improved version of the get_int function
# Much cleaner and it's more reusable
def improved_get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
    
main()