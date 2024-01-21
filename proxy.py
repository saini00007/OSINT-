import requests
from itertools import cycle

def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def make_request(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        # You can handle the response as needed
        print(f"Proxy: {proxy}, Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error with proxy {proxy}: {e}")

proxy_file_path = 'proxy.txt'
proxy_list = read_proxies_from_file(proxy_file_path)


proxy_cycle = cycle(proxy_list)

url_to_scrape = "https://httpbin.org/ip"
current_proxy = next(proxy_cycle)
make_request(url_to_scrape, current_proxy)
