import requests
from bs4 import BeautifulSoup
import re
import json
#---------------------------------------------------------------------------------------------------------------------------------------

# Scraping and getting any hint of data from this web was quite challenging as I keep trying to get clean data
# There are several things to have in mind here:
  # The original referred url when you click a boss match in the web leads you to this url: https://gw2wingman.nevermindcreations.de/log...
  # The web is divided by an <iframe> tag, where the iframe has an href leading to /logContent/...
  # Here is where we find most of the information as a table, however, I couldn't manage to retrieve that data yet
    # If we enter the logContent html we can see that the table info is in /html/body/div, in a div with id="content" and class="ei-container-small"
    # Inside this div, and after navigating through many div tags, we can find one marked as <div id="dps-table_wrapper" class="dataTables_wrapper">
    # And once more, inside this div we can find the table elements
    
# There are some problems getting the data as the source code and the html displayed by the google html tool(F12) is not equal
  # When doing requests of the web page and making any kind of search, BeautifulSoup is hardly able to find the necessary data as some of it is in a JS format
# All of this is part of experimentation and practice, so I should find a better way of retrieving the data

# However, back to code part, we will create both a constant URL and a headers variable:
URL = 'https://gw2wingman.nevermindcreations.de/logContent/20220823-171406_vg_kill'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# We request the web and create the soup variable
# Something I might try here is changing the parsing method to lxml instead of html.parser and trying to find the data by its XPath
req = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')

# This search is quite dirty as I had to count and get my desired script, but it's the eigth one on the url: https://gw2wingman.nevermindcreations.de/log/20220823-171406_vg_kill
  # Yes, I'm searching on the wrong url, but I had to try and retrieve some data to see if it could work
# I created a patter to search for an specific script; surprise, not working as expected: patternVar = re.compile('var _logData = (.*?);$')
data = soup.find_all('script')[8]

# We will write a json file with the data from our script called _logData
with open('vg_kill.json', 'w') as f:
    jsonFile = f.write(data.text.rstrip())
print(json.loads(jsonFile))

# From here and on it's a matter of trying different things to get cleaner data as the tables have the info I need and I could say they are my goal right now
# I have to thank this line: print(data.get('src'))
  # It got me to logContent source, which I've looked for
# I will post what the json loaded on the file, however, it is not pretty 
