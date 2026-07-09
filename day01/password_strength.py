def main():
    password = input("Input your password: ")
    
    if is_pass_strong(password):
        print("Your password is strong")
    else:
        print("Your Password is weak")

def is_pass_strong(password):
    if len(password) < 8:
        return False
    
    return is_verified(password)

def is_verified(password):
    is_digit = False
    is_lower = False
    is_upper = False
    for char in password:
        if char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char.isdigit():
            is_digit = True
        
        if is_lower and is_upper and is_digit:
            return True
    return False

main()