import requests

def shorten_url_tinyurl(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
long_url = input("Enter the long URL to shorten using TinyURL: ")
short_url = shorten_url_tinyurl(long_url)
if short_url:
    print(f"Shortened URL using TinyURL: {short_url}")
