#----------------IMPORTS-----------------
import requests
from bs4 import BeautifulSoup
import re

#----------------MAIN FUNCTION-----------------

def extract(url):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

    response = requests.get(url, HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = soup.find_all('script')[8]
    dataString = data.text.rstrip()

    logData = re.findall(r'{.*}', dataString)
    
    for line in logData:
        jsonFile = line
        
    return jsonFile

class boss:

    def __init__(self, url: str) -> str:
        self.url = url

    def getBossName(self) -> str:
        url = self.url
        urlLines = url.split('/')
        if len(urlLines) < 5:
            bossName = urlLines[3]
        elif len(urlLines) == 5:
            bossName = urlLines[4]
        return bossName
    
    def getBossTag(self, bossName: str) -> str:
        bossTag = bossName.split('_')
        nameTag = bossTag[1]
        return nameTag
        
#-------------BOSS-CLASS---------------

print(type(boss('https://gw2wingman.nevermindcreations.de/log/20221008-212527_matt_kill')))

bossName = boss('https://gw2wingman.nevermindcreations.de/log/20221008-212527_matt_kill').getBossName()
print(type(bossName))
print(bossName) 
# When we create the actual object and get its bossName method, we should store it in a variable so we can use it later on

bossTag = boss('https://gw2wingman.nevermindcreations.de/log/20221008-212527_matt_kill').getBossTag(bossName)
print(type(bossTag))
print(bossTag)
# Here we call getBossTag method and pass our previous bossName variable as an argument