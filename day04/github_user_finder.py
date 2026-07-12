import sys
from username_finder import search_github_user

def main():
    if len(sys.argv) < 2: 
        sys.exit("Too few arguments")
    
    search_github_user(sys.argv[1])

main()