def main():
    try:
        url_list = []
        
        tld_set = open_tld_file()

        url_list = url_file_opener("test_url_input.txt", tld_set)
        print(url_list)
    except FileNotFoundError:
        print("Error: Valid TLD List file not found")

def url_sanitizer(url, tld_set):
    if url.startswith(("http", "https")):
        url = url.removeprefix("https://").removeprefix("http://")
    if url.startswith("www"):
        url = url.removeprefix("www.")
    if url.endswith("/"):
        url = url.rstrip("/")

    if(not url_is_valid(url, tld_set)):
        raise ValueError("Value is not valid")

    return url


def url_is_valid(url, tld_set):
    if " " in url:
        return False
    
    splitted_url = url.split(".")
    length = len(splitted_url) - 1

    return True if splitted_url[length] in tld_set else False

def input_to_file(url):
    with open("sanitized_url.txt", "a") as file:
        url = url + "\n"
        file.write(url)
        print("URL Input Success")

def url_file_opener(filename, tld_set):
    try:
        url_list = []
        url_total = 0
        with open(filename) as file:
            for line in file:
                try:
                    url_total += 1
                    valid_url = url_sanitizer(line.strip(), tld_set)
                    url_list.append(valid_url)
                except ValueError:
                    print(f"Error: Url {line} is not valid, skipping to next line")
        success_url = len(url_list)
        print(f"Success: {success_url} Failure: {url_total - success_url}")
        return url_list
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return []

def open_tld_file():
    tld_set = set()
    with open("tld_list.txt") as file:
        for line in file:
            tld_set.add(line.strip())
    return tld_set

if __name__ == "__main__":
    main()