def main():
    validate_port()

def validate_port(port = 0):
    # an int will automatically raise a ValueError if the type is other than int
    port = int(port)
    if(port < 1 or port > 65535):
        raise ValueError("The Value should be in the range of 1 to 65535")
    print("Doing some scanning..")

if __name__ == "__main__":
    main()