from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
import time
import requests
import socket

def returnProxyHttp(ip, port):
    proxies = {"http": f"http://{ip}:{port}"}
    return proxies

def returnProxyHttps(ip, port):
    proxies = {"https": f"https://{ip}:{port}"}
    return proxies

https_proxies = [
    {"ip": "216.169.73.65", "port": "34679"},
    # {"ip": "81.23.114.238", "port": "8080"}
]

http_proxies = [
    {"ip": "95.182.78.6", "port": "5678"},
    {"ip": "182.253.158.181", "port": "5678"},
    {"ip": "12.186.205.123", "port": "80"},
]

socks5_proxies = [
    "socks5://162.241.115.85:54159"
]

def returnProxySocks5(link):
    return {"https" : f"{link}"}
    

def fetch(url, path):
    
    for proxy in socks5_proxies:
        try:
            print(returnProxySocks5(proxy))
            time.sleep(5)
            r = requests.get(url=url, proxies=returnProxySocks5(proxy))
            print(r)

            if r.status_code == 200:
                break
        except (requests.RequestException, socket.error) as e:
            print(f"{e} at {proxy}")
            continue
            
        print("Error ocurred requests.exceptions.ProxyError")

    if r.status_code != 200:
        print("Something is wrong; status code is not 200")

    with open(path, "w") as f:
        f.write(r.text)

fetch("https://indianexpress.com/section/india/", "../scrappingWebsite/scrapedData/index.html")
