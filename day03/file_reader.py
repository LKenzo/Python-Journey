def main():
    search_file()

def search_file():
    while True:
        try:
            filename = input("Enter filename: ").strip()
            with open(filename) as file:
                content = file.read()
        except FileNotFoundError:
            print("File not found.")
        else:
            print(content)
            break


main()