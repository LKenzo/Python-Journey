def main():
    menu()

def menu():
    while(True):
        print("1. Store name in file")
        print("2. Read file")
        print("3. Close program")
        choice = int(input("Please input a number: "))

        if (choice == 1) :
            store_name()
        elif(choice == 2):
            open_file()
        elif(choice == 3):
            return

def store_name():
    name = input("What's your name? ")

    with  open("names.txt", "a") as file:
        file.write(f"{name}\n")

def open_file():
    names = []
    with open("names.txt", "r") as file:
        for line in file:
            names.append(line.rstrip())
    
    for name in sorted(names):
        print(f"Hello, {name}")

if __name__ == "__main__":
    main()