import requests

url = "https://en.wikipedia.org/wiki/IPhone"

res = requests.get(url)

print(res)