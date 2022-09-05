#---------------------REQUESTS + BS4----------------------

import requests
from bs4 import BeautifulSoup
import re
import json

URL = 'https://gw2wingman.nevermindcreations.de/logContent/20220823-171406_vg_kill'
# Looking on the url we can clearly see that the info is inside an <iframe> tag
# Best option here was getting the src of the iframe and using the relative path (/logContent instead of /log)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
# User-Agent headers can be found here: https://deviceatlas.com/blog/list-of-user-agent-strings

req = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())
# .prettyfy() will show the content as a html written text
body = soup.find('body', class_='theme-slate')
print(body)

tdps = body.find('div', class_='dataTables_wrapper')
print(tdps)

div = body.find_all('div')
print(len(list(div)))


#patternVar = re.compile('var _logData = (.*?);$')
data = soup.find_all('script')[8]

with open('vg_kill.json', 'w') as f:
    jsonFile = f.write(data.text.rstrip())
print(json.loads(jsonFile))
#print(defData)
#print(data)
#allData = data.find('document')
#print(data.get('src'))



#---------------------SELENIUM----------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_PATH = 'C:\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

options = Options()
options.headless = True
options.add_argument('--window-size=1920,1000')
driver = webdriver.Chrome(options=options)

# url = 'https://gw2wingman.nevermindcreations.de//logContent/20220823-171406_vg_kill' 
driver.get('https://gw2wingman.nevermindcreations.de//logContent/20220823-171406_vg_kill')
# content = driver.page_source
# print(content)
# driver.quit()

#------------------------------------------------------
from os import path
from pathlib import PurePath
import sys

def url_download(urls, dir):
    paths = []

    for url in urls:
        url_name = PurePath(url).name
        url_path = path.join(dir, url_name)
        text = ''
    
        try:
            req = requests.get(url)
            if req.ok:
                text = req.text
            else:
                print('Error', req.status_code)
        except Exception as e:
            print(str(e))
        
        with open(f'{url_path}.txt', 'w') as f:
            f.write(text)
    
        paths.append(url_path)
    
    return paths

def download(urls):
    return url_download(urls, '.') 

def html_parse(path):
    with open(path, 'r') as f:
        content = f.read()

    return BeautifulSoup(content, 'html.parser') 

print(download('https://gw2wingman.nevermindcreations.de/logContent/20220823-171406_vg_kill'))