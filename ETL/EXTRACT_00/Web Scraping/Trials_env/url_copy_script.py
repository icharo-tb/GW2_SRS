import requests
from bs4 import BeautifulSoup

URL = 'https://gw2wingman.nevermindcreations.de/content/raid/dhuum'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

response = requests.get(URL,HEADERS)
soup = BeautifulSoup(response.content,'html.parser')

fh = open('urls.txt', 'w')

for link in soup.find_all('a'):
    url_str = 'https://gw2wingman.nevermindcreations.de'
    data = link.get('href')
    
    try:
        log_str = url_str+data
        fh.write(log_str)
        fh.write('\n')
    except Exception as e:
        print('Error: ', str(e))

fh.close()