import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import re
import json
#--------------------------------------------------------

# IMPORTANT: This can be all transformed into a fucntion, I have to find the way to connect everything

# Setting of connections such as the url and the headers
# Creation of the requests and the soup to explore the data (Bonus: checking the response code)

URL = 'https://dps.report/HUeg-20220829-210824_gors'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

# print(response.status_code) -> Response = 200
#--------------------------------------------------------

# Inside the html /logContent and dps.report urls we can find an eight script containing our json information
# We shall get that data in a text format and rstrip it to get it as cleaner as possible since it is contained on a JS variable
# Finally, we use re.findall() to get only the JSON dictionary containing all the boss info

data = soup.find_all('script')[8]
dataString = data.text.rstrip()

logData = re.findall(r'{.*}', dataString)

# XPath = /html/head/script[9]/text() -> Saved just in case
#--------------------------------------------------------

# Instead of typing manually every boss name for every file, we can search it in the url, with this basic condition:
    # There are 2 kinds of urls on GW2 Wingman [/logContent and dps.report]:
    # Therefore, we split the url, and based on it's lenght we will get the correct name

urlLines = URL.split('/')
if len(urlLines) < 5:
    bossName = urlLines[3]
elif len(urlLines) == 5:
    bossName = urlLines[4]
#--------------------------------------------------------

# We will write a new file containing all the info we gathered
# We iterate over the list created by the re.findall
# We will name the file based on the name on the url with the previous code

with open(f'{bossName}.json', 'w') as f:
    for line in logData:
        jsonFile = f.write(line)
    #json.loads(jsonFile)
    print('Done!')
#--------------------------------------------------------

# From here and under we can see different approaches that didn't work as expected
# They were a great help to learn 

    # with open('vg_kill.json', 'w') as f:
    #     jsonFile = f.write(dataString)
    # print(json.loads(jsonFile))
    #--------------------------------------------------------

    # table_1 = soup.find("table", id="dps-table") # Table id='dps-table'
    # columns = []
    # for i in table_1.find_all("th"):
    #     column_name = i.text
    #     columns.append(column_name)
    # print(columns)
    #--------------------------------------------------------

    # dom = etree.HTML(str(soup))
    # print(dom.xpath('//*[@id="dps-table"]/tbody/tr[1]/td[4]')[0].text)