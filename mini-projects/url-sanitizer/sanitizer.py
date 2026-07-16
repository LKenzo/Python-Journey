def main():
    sanitized_url = url_sanitizer(input("Input the URL: ").strip)
    print(f"Sanitized Url: {sanitized_url}")

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
    return True if "." in url else False


if __name__ == "__main__":
    main()