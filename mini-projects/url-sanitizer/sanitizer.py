def main():
    sanitized_url = url_sanitizer(input("Input the URL: ").strip())
    input_to_file(sanitized_url)

def url_sanitizer(url):
    if url.startswith(("http", "https")):
        url = url.removeprefix("https://").removeprefix("http://")
    if url.startswith("www"):
        url = url.removeprefix("www.")
    if url.endswith("/"):
        url = url.rstrip("/")

    if(not url_is_valid(url)):
        raise ValueError("Value is not valid")

    return url

def url_is_valid(url):
    if " " in url:
        return False
    
    splitted_url = url.split(".")
    length = len(splitted_url) - 1
    with open("tld_list.txt") as file:
        for valid_tld in file:
            if splitted_url[length] == valid_tld.strip():
                return True
            
    return False

def input_to_file(url):
    with open("sanitized_url.txt", "a") as file:
        url = url + "\n"
        file.write(url)
        print("URL Input Success")

if __name__ == "__main__":
    main()