import sys

hex_signatures = {
    "25504446": "pdf",
    "4D5A": "exe",
    "89504E470D0A1A0A": "png",
    "FFD8FFDB": "jpg",
    "FFD8FFE0": "jpg",
    "504B0304": "zip"
}

def main():
    if len(sys.argv) == 2:
        hex_string = file_opener(sys.argv[1])
        result = file_identifier(hex_string)
        
        if result == None:
            print("Error: The file byte signature is not on the list")
            return
        print(f"The file type is {result}")

    else:
        print("Error: Please provide a filename to check")

def file_opener(filename):
    try:
        with open(filename, "rb") as file:
            hex_string = file.read(8).hex().upper()
        return hex_string
    except FileNotFoundError:
        sys.exit(f"Error: File {filename} was not found.")

def file_identifier(hex_string):
    current_hex = ""
    
    #The use of this loop is to check if it matches with one of the signatures and increment it by 2 hex characters each time.
    for i in range(0, len(hex_string), 2):
        current_hex += hex_string[i:i+2] 
        if current_hex in hex_signatures:
            return hex_signatures[current_hex]
    return

if __name__ == "__main__":
    main()