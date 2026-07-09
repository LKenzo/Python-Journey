def main():
    password = input_password()
    password_guesser(password)
        

def input_password():
    password = input("Input your super secret password: ")
    return password

def password_guesser(user_password):
    #This list can be changed to a common password txt file
    password_list = [
        "apple", "gacor123", "yellow", "brown123", "admin123"
    ]

    #iterate over the string inside of the list
    for password in password_list:
        print("Guess:")
        print(password)

        if password == user_password:
            print("Correct!")
            return
        print("Wrong.\n")

    return


main()