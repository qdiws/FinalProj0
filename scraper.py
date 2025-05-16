import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if 'x.com' in a['href']]
    return links

start_url = "https://x.com"
network_data = []
links = get_links(start_url)
for link in links:
    network_data.append({'source': start_url, 'target': link})

df = pd.DataFrame(network_data)
df.to_csv("web_traffic_data.csv", index=False)
