def main():
    password = input_password()
    password_guesser(password)
        

def input_password():
    password = input("Input your super secret password: ")
    return password

def password_guesser(user_password):
    #There are two option of opening a file and i prefer using with
    with open("password_list.txt") as file:

        #iterate over the string inside of the file
        for password_candidate in file:
            password_candidate.strip()

            print("Guess:")
            print(password_candidate)

            if password_candidate == user_password:
                print("Correct!")
                return
            print("Wrong.\n")

        print("Password was not found.")
        return


main()