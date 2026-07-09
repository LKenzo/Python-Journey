def hello():
    print("hello")

# Ask user for their  name
name = input("What's your name? ")

#Can be used like this too
# name = input("What's your name? ").strip().title()

#Remove Whitespace from str
name = name.strip()

#Capitalize user's name (.capitalize() can be used too)
name = name.title()

# Say hello to user
# print("Hello, ", name, sep="???")
print("Hello, ", end="")
print("\"" + name  + "\"")

# Ask user Age
age = input("What's your age? ")

# Say user Age
print(f"Your age is {age}")

# Splitting user's name into first name and last name
first, last = name.split(" ")

print(f"Hello, {first}")