import requests

r = requests.get("https://www.backstage.com/talent/find-talent/models/", proxies={"https": "socks5://72.217.158.202:4145"})
print(r.text)