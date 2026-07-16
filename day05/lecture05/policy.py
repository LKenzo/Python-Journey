def main():
    if check_password(input("Input your password: ")):
        print("Your password is valid")
    else:
        print("Password is not correct") 
          

def check_password(password):
    return True if len(password) >= 8 and "!" in password else False

if __name__ == "__main__":
    main()