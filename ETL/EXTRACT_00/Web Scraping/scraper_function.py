import requests
from bs4 import BeautifulSoup
import re
#--------------------------------------------------------

def log_scrape(url):

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

    response = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = soup.find_all('script')[8]
    dataString = data.text.rstrip()

    logData = re.findall(r'{.*}', dataString)

    try:
        urlLines = url.split('/')
        if len(urlLines) < 5:
            bossName = urlLines[3]
        elif len(urlLines) == 5:
            bossName = urlLines[4]
    except Exception as e:
        return f'Error: {str(e)}'

    pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data' 

    with open(f'{pathName}\{bossName}.json', 'w') as f:
        for line in logData:
            jsonFile = f.write(line)
    return jsonFile
pass
#--------------------------------------------------------

print(log_scrape('https://gw2wingman.nevermindcreations.de/logContent/20220823-232523_kc_kill'))