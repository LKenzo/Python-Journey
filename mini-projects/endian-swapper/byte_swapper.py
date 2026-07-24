import sys

def main():
    # sys.argv[1] is the file and sys.argv[2] is the byte
    if len(sys.argv) == 3:
        hex_string = open_file(sys.argv[1])
        result_hex = endian_swapper(hex_string, int(sys.argv[2]))
        file_output(sys.argv[1], result_hex)
    else:
        print("Error: python endian_swapper.py <filename> <byte_length>")

def open_file(filename):
    try:
        with open(filename, "rb") as file:
            hex_string = file.read().hex()
        return hex_string
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def endian_swapper(hex_string, length):
    result_hex = ""
    for num in range(0, len(hex_string), length * 2):
        hex_pairs = []
        hex_block = hex_string[num:num + length * 2]

        #split each byte
        for i in range(0, len(hex_block), 2):
            hex_pairs.append(hex_block[i:i + 2])

        hex_pairs.reverse()
        joined_hex = "".join(hex_pairs)
        result_hex += joined_hex
    return result_hex

def file_output(filename, result_hex):
    result_file = "repaired_" + filename
    with open(result_file, "wb") as file:
        file.write(bytes.fromhex(result_hex))
    print(f"Successfuly save result to {result_file}")

if __name__ == "__main__":
    main()
