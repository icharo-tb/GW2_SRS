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
        return 'Error' + str(e)
    
    tag = bossName.split('_')
    bossTag = tag[1]

    global pathName


    # Wing_1
    if bossTag == 'vg':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_1\Valley_Guardian'
    elif bossTag == 'gors':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_1\Gorseval_The_Multifarious'
    elif bossTag == 'sab':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_1\Sabetha'
    # Wing_2
    elif bossTag == 'sloth':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_2\Slothasor'
    elif bossTag == 'matt':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_2\Mathias'
    # Wing_3
    elif bossTag == 'kc':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_3\Keep_Construct'
    elif bossTag == 'xera':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_3\Xera'
    # Wing_4
    elif bossTag == 'cairn':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_4\Cairn_The_Indomitable'
    elif bossTag == 'mo':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_4\Mursaat_Overseer'
    elif bossTag == 'sam':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_4\Samarog'
    elif bossTag == 'dei':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_4\Deimos'
    # Wing_5
    elif bossTag == 'sh':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_5\Soulless_Horror_Deesmina'
    elif bossTag == 'dhuum':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_5\Dhuum'
    # Wing_6
    elif bossTag == 'ca':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_6\Conjured_Amalgamate'
    elif bossTag == 'twinlargos' or 'twins':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_6\Twin_Largos'
    elif bossTag == 'qadim':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_6\Qadim'
    # Wing_7
    elif bossTag == 'adina':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_7\Cardinal_Adina'
    elif bossTag == 'sabir':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_7\Cardinal_Sabir'
    elif bossTag == 'prlqadim' or bossTag == 'qpeer':
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_7\Qadim_The_Peerless'
    else:
        pathName = 'ETL\EXTRACT_00\Web Scraping\Boss_data'

    with open(f'{pathName}\{bossName}.json', 'w') as f:
        for line in logData:
            jsonFile = f.write(line)
    
    return jsonFile
pass
#--------------------------------------------------------

# with open('gw2_urls.txt', 'r') as f:
#     urls = f.readlines()
#     for url in urls:
#         print(log_scrape(url))
#--------------------------------------------------------

print(log_scrape('https://gw2wingman.nevermindcreations.de/logContent/20220830-230417_dei_kill'))