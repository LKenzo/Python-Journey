# import json
import requests

def main():
    search_github_user("torvalds")

def search_github_user(username):
    
    response = requests.get("https://api.github.com/users/" + username)
    if response.status_code == 404:
        print("Username not found")
        return
    
    output = response.json()
    bio = output.get("bio") or "No bio available"

    # print(json.dumps(output, indent=2))
    print(f"Username: {username}")
    print(f"Followers: {output["followers"]}")
    print(f"Following {output["following"]}")
    print(f"Public repos: {output["public_repos"]}")
    print(f"Bio: {bio}")
    

        

if __name__ == "__main__":
    main()