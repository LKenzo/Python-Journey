def main():
    username = input("Username: ")
    password = input("Password: ")
    
    if account_verifier(username, password):
        print("Welcome")
    else:
        print("Access Denied")

def account_verifier(username, password):
    return True if username == "Max" and password == "123" else False

main()