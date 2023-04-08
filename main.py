import requests
import json

API_KEY = "bbf5572d8f0a915b92a8f60f7cf92fa92046e"

def shorten_url(long_url):
    url = "https://cutt.ly/api/api.php"
    params = {
        "key": API_KEY,
        "short": long_url
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)["url"]
    if data["status"] == 7:
        return data["shortLink"]
    else:
        raise Exception(data["errorMessage"])


long_url = input('Enter Link: ')
short_url = shorten_url(long_url)
print("Shortened URL:", short_url)