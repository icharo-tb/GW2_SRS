import requests
from bs4 import BeautifulSoup

# In order to make things faster, we will search for hrefs on each boss:
    # For each boss we should add /content before /raid, it will take us to the actual HTML page filled with logs
    # We can then freely search, although most of the logs will be stored in <a> tags
    # For instance: hrefs contain an apikey and JS hrefs as well, so we will ignore them
    # Now, we could use write mode ('w') to make the URL file, however, this will end up being slow
    # Instead, we will use append mode ('a'), and with the help of our "ignore this lines", it will append only actual logs
    # We just need to add two more things:
        # In order for the EXTRACT algorithm to work properly, for each href link, we will add the https from Wingman web
        # We will set a newline for every link, so lines do not appear together as a single line

URL = 'https://gw2wingman.nevermindcreations.de/content/raid/xera'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

response = requests.get(URL,HEADERS)
soup = BeautifulSoup(response.content,'html.parser')

fh = open(r'C:\Users\DANIEL\workspace\gw2_srs\GW2_SRS\ETL\EXTRACT_00\Web Scraping\Trials_env\urls.txt', 'a')

for link in soup.find_all('a'):
    url_str = 'https://gw2wingman.nevermindcreations.de'
    data = link.get('href')
    
    try:
        log_str = url_str+data
        if log_str.endswith('apikey'):
            log_str.replace('apikey','\n')
        elif log_str.endswith('void(0)'):
            log_str.replace('void(0)','\n')
        else:
            fh.write(log_str)
            fh.write('\n')
    except Exception as e:
        print('Error: ', str(e))

fh.close()